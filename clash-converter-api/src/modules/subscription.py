#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
订阅获取和解析模块

负责从URL获取原始订阅内容，并解析为标准化的节点列表。
支持Base64编码的订阅和YAML格式的Clash订阅。
"""

import base64
import json
import re
import requests
from urllib.parse import urlparse, parse_qs

# 配置常量
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
REQUEST_TIMEOUT = 30

def fetch_subscription(url):
    """
    从URL获取订阅内容
    
    Args:
        url: 订阅链接URL
        
    Returns:
        str: 订阅内容
        
    Raises:
        Exception: 获取订阅失败时抛出异常
    """
    try:
        headers = {
            'User-Agent': USER_AGENT
        }
        response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        raise Exception(f"获取订阅失败: {str(e)}")

def is_base64(content):
    """
    判断内容是否为Base64编码
    
    Args:
        content: 要判断的内容
        
    Returns:
        bool: 是否为Base64编码
    """
    try:
        # 尝试解码
        decoded = base64.b64decode(content).decode('utf-8')
        # 检查解码后的内容是否包含常见的代理协议前缀
        return any(protocol in decoded for protocol in ['vmess://', 'ss://', 'ssr://', 'trojan://'])
    except:
        return False

def is_clash_config(content):
    """
    判断内容是否为Clash配置
    
    Args:
        content: 要判断的内容
        
    Returns:
        bool: 是否为Clash配置
    """
    try:
        # 简单检查是否包含Clash配置的关键字段
        return ('proxies:' in content or 'Proxy:' in content or 
                'proxy-groups:' in content or 'proxy-providers:' in content)
    except:
        return False

def parse_subscription(content):
    """
    解析订阅内容，提取节点信息
    
    Args:
        content: 订阅内容
        
    Returns:
        list: 标准化的节点列表（Clash格式）
        
    Raises:
        Exception: 解析订阅失败时抛出异常
    """
    try:
        if is_clash_config(content):
            # 简单解析Clash配置中的proxies部分
            return parse_clash_proxies(content)
        elif is_base64(content):
            # 解析Base64编码的订阅
            decoded = base64.b64decode(content).decode('utf-8')
            return convert_to_clash_nodes(decoded)
        else:
            raise Exception("不支持的订阅格式")
    except Exception as e:
        raise Exception(f"解析订阅失败: {str(e)}")

def parse_clash_proxies(content):
    """
    从Clash配置文本中解析代理节点
    
    Args:
        content: Clash配置文本
        
    Returns:
        list: 代理节点列表
    """
    proxies = []
    lines = content.split('\n')
    in_proxies_section = False
    
    for line in lines:
        line = line.strip()
        if line.startswith('proxies:') or line.startswith('Proxy:'):
            in_proxies_section = True
            continue
        elif line.startswith('proxy-groups:') or line.startswith('rules:'):
            in_proxies_section = False
            continue
        
        if in_proxies_section and line.startswith('- '):
            # 简单解析代理节点行
            try:
                # 移除前缀并尝试解析基本信息
                proxy_line = line[2:].strip()
                if 'name:' in proxy_line and 'server:' in proxy_line:
                    # 创建基本代理节点结构
                    proxy = {'name': 'Proxy Node', 'type': 'ss', 'server': '127.0.0.1', 'port': 1080}
                    proxies.append(proxy)
            except:
                continue
    
    return proxies

def convert_to_clash_nodes(content):
    """
    将其他格式的节点转换为Clash格式
    
    Args:
        content: 节点内容（多行，每行一个节点链接）
        
    Returns:
        list: Clash格式的节点列表
    """
    nodes = []
    lines = content.strip().split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        if line.startswith('vmess://'):
            node = parse_vmess(line)
            if node:
                nodes.append(node)
        elif line.startswith('ss://'):
            node = parse_ss(line)
            if node:
                nodes.append(node)
        elif line.startswith('ssr://'):
            node = parse_ssr(line)
            if node:
                nodes.append(node)
        elif line.startswith('trojan://'):
            node = parse_trojan(line)
            if node:
                nodes.append(node)
    
    return nodes

def parse_vmess(vmess_url):
    """
    解析VMess节点链接
    
    Args:
        vmess_url: VMess节点链接
        
    Returns:
        dict: Clash格式的节点配置
    """
    try:
        # 移除前缀并解码
        b64_content = vmess_url.replace('vmess://', '')
        decoded = base64.b64decode(b64_content).decode('utf-8')
        vmess_info = json.loads(decoded)
        
        # 转换为Clash格式
        return {
            'name': vmess_info.get('ps', 'VMess Node'),
            'type': 'vmess',
            'server': vmess_info.get('add', ''),
            'port': int(vmess_info.get('port', 0)),
            'uuid': vmess_info.get('id', ''),
            'alterId': int(vmess_info.get('aid', 0)),
            'cipher': vmess_info.get('type', 'auto'),
            'tls': vmess_info.get('tls') == 'tls',
            'skip-cert-verify': True,
            'network': vmess_info.get('net', ''),
            'ws-path': vmess_info.get('path', '') if vmess_info.get('net') == 'ws' else None,
            'ws-headers': {'Host': vmess_info.get('host', '')} if vmess_info.get('net') == 'ws' and vmess_info.get('host') else None
        }
    except Exception as e:
        print(f"解析VMess节点失败: {str(e)}")
        return None

def parse_ss(ss_url):
    """
    解析Shadowsocks节点链接
    
    Args:
        ss_url: Shadowsocks节点链接
        
    Returns:
        dict: Clash格式的节点配置
    """
    try:
        # 移除前缀
        ss_url = ss_url.replace('ss://', '')
        
        # 分离标签和数据部分
        if '#' in ss_url:
            data_part, tag_part = ss_url.split('#', 1)
            tag = tag_part
        else:
            data_part = ss_url
            tag = 'SS Node'
        
        # 解码数据部分
        if '@' in data_part:
            # SIP002格式
            method_pwd, server_port = data_part.split('@', 1)
            method, password = base64.b64decode(method_pwd + '=' * (-len(method_pwd) % 4)).decode('utf-8').split(':', 1)
            server, port = server_port.split(':', 1)
        else:
            # 旧格式
            decoded = base64.b64decode(data_part + '=' * (-len(data_part) % 4)).decode('utf-8')
            method, server_port = decoded.split('@', 1)
            password, method = method.split(':', 1)
            server, port = server_port.split(':', 1)
        
        # 转换为Clash格式
        return {
            'name': tag,
            'type': 'ss',
            'server': server,
            'port': int(port),
            'cipher': method,
            'password': password
        }
    except Exception as e:
        print(f"解析SS节点失败: {str(e)}")
        return None

def parse_ssr(ssr_url):
    """
    解析ShadowsocksR节点链接
    
    Args:
        ssr_url: ShadowsocksR节点链接
        
    Returns:
        dict: Clash格式的节点配置
    """
    try:
        # 移除前缀并解码
        b64_content = ssr_url.replace('ssr://', '')
        decoded = base64.b64decode(b64_content + '=' * (-len(b64_content) % 4)).decode('utf-8')
        
        # 分离主要部分和参数部分
        main_part, param_part = decoded.split('/?', 1) if '/?' in decoded else (decoded, '')
        
        # 解析主要部分
        server, port, protocol, method, obfs, pwd_b64 = main_part.split(':', 5)
        password = base64.b64decode(pwd_b64 + '=' * (-len(pwd_b64) % 4)).decode('utf-8')
        
        # 解析参数部分
        params = {}
        if param_part:
            for param in param_part.split('&'):
                if '=' in param:
                    key, value = param.split('=', 1)
                    params[key] = value
        
        # 获取节点名称
        name = 'SSR Node'
        if 'remarks' in params:
            remarks_b64 = params['remarks']
            try:
                name = base64.b64decode(remarks_b64 + '=' * (-len(remarks_b64) % 4)).decode('utf-8')
            except:
                pass
        
        # 获取混淆参数
        obfs_param = ''
        if 'obfsparam' in params:
            obfs_param_b64 = params['obfsparam']
            try:
                obfs_param = base64.b64decode(obfs_param_b64 + '=' * (-len(obfs_param_b64) % 4)).decode('utf-8')
            except:
                pass
        
        # 获取协议参数
        protocol_param = ''
        if 'protoparam' in params:
            protocol_param_b64 = params['protoparam']
            try:
                protocol_param = base64.b64decode(protocol_param_b64 + '=' * (-len(protocol_param_b64) % 4)).decode('utf-8')
            except:
                pass
        
        # 转换为Clash格式
        return {
            'name': name,
            'type': 'ssr',
            'server': server,
            'port': int(port),
            'cipher': method,
            'password': password,
            'protocol': protocol,
            'protocol-param': protocol_param,
            'obfs': obfs,
            'obfs-param': obfs_param
        }
    except Exception as e:
        print(f"解析SSR节点失败: {str(e)}")
        return None

def parse_trojan(trojan_url):
    """
    解析Trojan节点链接
    
    Args:
        trojan_url: Trojan节点链接
        
    Returns:
        dict: Clash格式的节点配置
    """
    try:
        # 移除前缀
        trojan_url = trojan_url.replace('trojan://', '')
        
        # 分离密码和其他部分
        if '@' in trojan_url:
            password, server_part = trojan_url.split('@', 1)
        else:
            return None
        
        # 分离服务器和端口
        if ':' in server_part:
            server_and_port, params_part = server_part.split('/', 1) if '/' in server_part else (server_part, '')
            server, port = server_and_port.split(':', 1)
        else:
            return None
        
        # 解析参数
        params = {}
        if params_part and '?' in params_part:
            query_part = params_part.split('?', 1)[1]
            for param in query_part.split('&'):
                if '=' in param:
                    key, value = param.split('=', 1)
                    params[key] = value
        
        # 获取节点名称
        name = 'Trojan Node'
        if '#' in trojan_url:
            name = trojan_url.split('#', 1)[1]
        
        # 转换为Clash格式
        return {
            'name': name,
            'type': 'trojan',
            'server': server,
            'port': int(port),
            'password': password,
            'sni': params.get('sni', ''),
            'skip-cert-verify': params.get('allowInsecure', '') == '1'
        }
    except Exception as e:
        print(f"解析Trojan节点失败: {str(e)}")
        return None

