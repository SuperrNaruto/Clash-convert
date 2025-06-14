import { useState, useEffect } from 'react'
import './App.css'

// API 基础地址可通过环境变量 VITE_API_BASE_URL 配置
// 默认为與當前網站同源的 `/api` 路徑
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api'

function App() {
  const [activeTab, setActiveTab] = useState('convert')
  const [subscriptionUrl, setSubscriptionUrl] = useState('')
  const [outputFilename, setOutputFilename] = useState('clash_config.yaml')
  const [selectedGroups, setSelectedGroups] = useState(['streaming', 'social', 'ai', 'adblock'])
  const [groupTypes, setGroupTypes] = useState({})
  const [isLoading, setIsLoading] = useState(false)
  const [result, setResult] = useState(null)
  const [error, setError] = useState(null)
  const [appInfo, setAppInfo] = useState(null)
  const [progress, setProgress] = useState(0)

  // 预设配置
  const presetConfigs = {
    default: {
      name: '默认配置',
      description: '流媒体、社交媒体、AI服务、广告拦截',
      groups: ['streaming', 'social', 'ai', 'adblock'],
      icon: '⚙️',
      color: 'blue'
    },
    entertainment: {
      name: '影音娱乐',
      description: '适合观看视频、听音乐的用户',
      groups: ['streaming', 'social', 'adblock'],
      icon: '🎬',
      color: 'purple'
    },
    developer: {
      name: '程序开发',
      description: '适合软件开发人员',
      groups: ['techgiants', 'developer', 'ai', 'adblock'],
      icon: '💻',
      color: 'green'
    },
    gaming: {
      name: '游戏玩家',
      description: '适合游戏爱好者',
      groups: ['gaming', 'social', 'streaming', 'adblock'],
      icon: '🎮',
      color: 'red'
    },
    business: {
      name: '商务办公',
      description: '适合商务和办公场景',
      groups: ['techgiants', 'finance', 'shopping', 'news', 'adblock'],
      icon: '💼',
      color: 'yellow'
    },
    all: {
      name: '全功能配置',
      description: '包含所有策略组，功能最全面',
      groups: ['streaming', 'social', 'ai', 'techgiants', 'gaming', 'finance', 'shopping', 'news', 'developer', 'adblock'],
      icon: '🚀',
      color: 'indigo'
    }
  }

  // 获取策略组类型
  useEffect(() => {
    fetchGroupTypes()
    fetchAppInfo()
  }, [])

  const fetchGroupTypes = async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/groups`)
      const data = await response.json()
      if (data.success) {
        setGroupTypes(data.groups)
      }
    } catch (error) {
      console.error('获取策略组类型失败:', error)
    }
  }

  const fetchAppInfo = async () => {
    try {
      const response = await fetch(`${API_BASE_URL}/info`)
      const data = await response.json()
      if (data.success) {
        setAppInfo(data.info)
      }
    } catch (error) {
      console.error('获取应用信息失败:', error)
    }
  }

  const simulateProgress = () => {
    setProgress(0)
    const interval = setInterval(() => {
      setProgress(prev => {
        if (prev >= 90) {
          clearInterval(interval)
          return 90
        }
        return prev + Math.random() * 15
      })
    }, 200)
    return interval
  }

  const handleConvert = async () => {
    if (!subscriptionUrl.trim()) {
      setError('请输入订阅链接')
      return
    }

    setIsLoading(true)
    setError(null)
    setResult(null)
    
    const progressInterval = simulateProgress()

    try {
      const response = await fetch(`${API_BASE_URL}/convert`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          subscription_url: subscriptionUrl,
          selected_groups: selectedGroups,
          output_filename: outputFilename
        })
      })

      const data = await response.json()
      
      clearInterval(progressInterval)
      setProgress(100)
      
      if (data.success) {
        setResult(data)
        setTimeout(() => setProgress(0), 1000)
      } else {
        setError(data.error || '转换失败')
        setProgress(0)
      }
    } catch (error) {
      clearInterval(progressInterval)
      setProgress(0)
      setError('网络错误: ' + error.message)
    } finally {
      setIsLoading(false)
    }
  }

  const handlePresetSelect = (presetKey) => {
    const preset = presetConfigs[presetKey]
    setSelectedGroups(preset.groups)
  }

  const handleGroupToggle = (groupId) => {
    setSelectedGroups(prev => 
      prev.includes(groupId) 
        ? prev.filter(id => id !== groupId)
        : [...prev, groupId]
    )
  }

  const downloadConfig = () => {
    if (!result) return
    
    const blob = new Blob([result.config_content], { type: 'text/yaml' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = result.filename
    document.body.appendChild(a)
    a.click()
    document.body.removeChild(a)
    URL.revokeObjectURL(url)
  }

  const getColorClasses = (color) => {
    const colors = {
      blue: 'border-blue-500 bg-blue-50 text-blue-700',
      purple: 'border-purple-500 bg-purple-50 text-purple-700',
      green: 'border-green-500 bg-green-50 text-green-700',
      red: 'border-red-500 bg-red-50 text-red-700',
      yellow: 'border-yellow-500 bg-yellow-50 text-yellow-700',
      indigo: 'border-indigo-500 bg-indigo-50 text-indigo-700'
    }
    return colors[color] || colors.blue
  }

  const renderConvertTab = () => (
    <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
      {/* 左侧：订阅配置 */}
      <div className="space-y-6">
        <div className="bg-white rounded-xl shadow-lg p-6 card-hover">
          <div className="flex items-center mb-4">
            <div className="bg-gradient-to-r from-blue-500 to-blue-600 rounded-lg p-3 mr-4">
              <span className="text-white text-2xl">📡</span>
            </div>
            <div>
              <h2 className="text-xl font-semibold text-gray-800">订阅配置</h2>
              <p className="text-sm text-gray-500">输入您的订阅链接开始转换</p>
            </div>
          </div>
          
          <div className="space-y-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                订阅链接 <span className="text-red-500">*</span>
              </label>
              <input
                type="url"
                value={subscriptionUrl}
                onChange={(e) => setSubscriptionUrl(e.target.value)}
                placeholder="https://your-subscription-url"
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all input-focus"
              />
            </div>
            
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                输出文件名
              </label>
              <input
                type="text"
                value={outputFilename}
                onChange={(e) => setOutputFilename(e.target.value)}
                placeholder="clash_config.yaml"
                className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all input-focus"
              />
            </div>
          </div>
        </div>

        {/* 预设配置 */}
        <div className="bg-white rounded-xl shadow-lg p-6 card-hover">
          <div className="flex items-center mb-4">
            <div className="bg-gradient-to-r from-purple-500 to-purple-600 rounded-lg p-3 mr-4">
              <span className="text-white text-2xl">⚙️</span>
            </div>
            <div>
              <h2 className="text-xl font-semibold text-gray-800">预设配置</h2>
              <p className="text-sm text-gray-500">选择适合您使用场景的配置</p>
            </div>
          </div>
          
          <div className="grid grid-cols-1 gap-3">
            {Object.entries(presetConfigs).map(([key, preset]) => (
              <button
                key={key}
                onClick={() => handlePresetSelect(key)}
                className={`p-4 text-left border-2 rounded-xl transition-all btn-hover ${
                  JSON.stringify(selectedGroups.sort()) === JSON.stringify(preset.groups.sort())
                    ? getColorClasses(preset.color)
                    : 'border-gray-200 hover:border-gray-300 bg-white'
                }`}
              >
                <div className="flex items-center mb-2">
                  <span className="text-2xl mr-3">{preset.icon}</span>
                  <div className="font-medium text-gray-800">{preset.name}</div>
                </div>
                <div className="text-sm text-gray-600">{preset.description}</div>
                <div className="mt-2 text-xs text-gray-500">
                  {preset.groups.length} 个策略组
                </div>
              </button>
            ))}
          </div>
        </div>

        {/* 转换按钮 */}
        <div className="relative">
          <button
            onClick={handleConvert}
            disabled={isLoading || !subscriptionUrl.trim()}
            className="w-full bg-gradient-to-r from-blue-600 to-blue-700 text-white py-4 px-6 rounded-xl font-medium hover:from-blue-700 hover:to-blue-800 disabled:from-gray-400 disabled:to-gray-500 disabled:cursor-not-allowed transition-all btn-hover shadow-lg"
          >
            {isLoading ? (
              <div className="flex items-center justify-center">
                <div className="animate-spin rounded-full h-5 w-5 border-b-2 border-white mr-3"></div>
                转换中...
              </div>
            ) : '🚀 开始转换'}
          </button>
          
          {/* 进度条 */}
          {isLoading && (
            <div className="mt-3">
              <div className="bg-gray-200 rounded-full h-2">
                <div 
                  className="progress-bar rounded-full h-2 transition-all duration-300"
                  style={{ width: `${progress}%` }}
                ></div>
              </div>
              <div className="text-center text-sm text-gray-600 mt-2">
                {progress < 30 ? '正在获取订阅内容...' :
                 progress < 60 ? '正在解析节点信息...' :
                 progress < 90 ? '正在生成配置文件...' : '即将完成...'}
              </div>
            </div>
          )}
        </div>

        {/* 已选择的策略组 */}
        <div className="bg-gradient-to-r from-gray-50 to-gray-100 rounded-xl p-4">
          <div className="flex items-center justify-between mb-3">
            <span className="font-medium text-gray-800">已选择 {selectedGroups.length} 个策略组</span>
            <div className="space-x-2">
              <button
                onClick={() => setSelectedGroups(Object.keys(groupTypes))}
                className="text-sm text-blue-600 hover:text-blue-800 font-medium"
              >
                全选
              </button>
              <button
                onClick={() => setSelectedGroups([])}
                className="text-sm text-red-600 hover:text-red-800 font-medium"
              >
                清除
              </button>
            </div>
          </div>
          <div className="flex flex-wrap gap-2">
            {selectedGroups.map(groupId => (
              <span key={groupId} className="inline-flex items-center px-3 py-1 bg-blue-100 text-blue-800 text-sm rounded-full font-medium">
                {groupTypes[groupId]?.icon} {groupTypes[groupId]?.name}
              </span>
            ))}
            {selectedGroups.length === 0 && (
              <span className="text-gray-500 text-sm">请选择至少一个策略组</span>
            )}
          </div>
        </div>
      </div>

      {/* 右侧：功能特性和结果 */}
      <div className="space-y-6">
        {!result && !error && (
          <div className="bg-white rounded-xl shadow-lg p-6 card-hover">
            <div className="flex items-center mb-4">
              <div className="bg-gradient-to-r from-green-500 to-green-600 rounded-lg p-3 mr-4">
                <span className="text-white text-2xl">✨</span>
              </div>
              <h2 className="text-xl font-semibold text-gray-800">功能特性</h2>
            </div>
            <div className="space-y-4">
              {[
                { icon: '📊', text: `${appInfo?.total_rulesets || 76}个高质量规则集`, color: 'text-blue-600' },
                { icon: '⚡', text: '智能缓存系统', color: 'text-yellow-600' },
                { icon: '🎯', text: '多种订阅格式支持', color: 'text-green-600' },
                { icon: '🔧', text: `${appInfo?.group_types || 10}种策略组分类`, color: 'text-purple-600' },
                { icon: '🌐', text: '响应式Web界面', color: 'text-indigo-600' }
              ].map((feature, index) => (
                <div key={index} className="flex items-center p-3 bg-gray-50 rounded-lg">
                  <span className="text-2xl mr-3">{feature.icon}</span>
                  <span className={`font-medium ${feature.color}`}>{feature.text}</span>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* 错误信息 */}
        {error && (
          <div className="bg-red-50 border-2 border-red-200 rounded-xl p-6 error-shake">
            <div className="flex items-center">
              <div className="bg-red-500 rounded-full p-2 mr-4">
                <span className="text-white text-xl">❌</span>
              </div>
              <div>
                <h3 className="font-semibold text-red-800 text-lg">转换失败</h3>
                <p className="text-red-600 mt-1">{error}</p>
              </div>
            </div>
          </div>
        )}

        {/* 转换结果 */}
        {result && (
          <div className="bg-green-50 border-2 border-green-200 rounded-xl p-6 success-checkmark">
            <div className="flex items-center mb-4">
              <div className="bg-green-500 rounded-full p-2 mr-4">
                <span className="text-white text-xl">✅</span>
              </div>
              <h3 className="text-xl font-semibold text-green-800">转换成功！</h3>
            </div>
            
            <div className="space-y-4 mb-6">
              <div className="grid grid-cols-2 gap-4">
                {[
                  { label: '节点数量', value: result.stats.proxies, icon: '🔗' },
                  { label: '策略组', value: result.stats.groups, icon: '📁' },
                  { label: '规则数量', value: result.stats.rules, icon: '📋' },
                  { label: '规则集', value: result.stats.rulesets, icon: '📦' }
                ].map((stat, index) => (
                  <div key={index} className="bg-white rounded-lg p-3 text-center">
                    <div className="text-2xl mb-1">{stat.icon}</div>
                    <div className="text-sm text-gray-600">{stat.label}</div>
                    <div className="font-bold text-lg text-gray-800">{stat.value}</div>
                  </div>
                ))}
              </div>
              
              <div className="bg-white rounded-lg p-4">
                <span className="text-gray-600 font-medium">选中策略组:</span>
                <div className="mt-2 flex flex-wrap gap-2">
                  {result.selected_groups.map((group, index) => (
                    <span key={index} className="inline-block px-3 py-1 bg-green-100 text-green-800 text-sm rounded-full font-medium">
                      {group}
                    </span>
                  ))}
                </div>
              </div>
            </div>

            <button
              onClick={downloadConfig}
              className="w-full bg-gradient-to-r from-green-600 to-green-700 text-white py-3 px-4 rounded-xl font-medium hover:from-green-700 hover:to-green-800 transition-all btn-hover shadow-lg"
            >
              📥 下载配置文件
            </button>
          </div>
        )}
      </div>
    </div>
  )

  const renderGroupsTab = () => (
    <div>
      <div className="mb-8 text-center">
        <h2 className="text-3xl font-bold text-gray-800 mb-3">策略组配置</h2>
        <p className="text-gray-600 text-lg">选择您需要的策略组类型，每种策略组包含相关的应用和服务分流规则</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {Object.entries(groupTypes).map(([groupId, group]) => (
          <div
            key={groupId}
            className={`bg-white rounded-xl shadow-lg p-6 cursor-pointer transition-all card-hover ${
              selectedGroups.includes(groupId)
                ? 'ring-4 ring-blue-500 bg-blue-50 transform scale-105'
                : 'hover:shadow-xl'
            }`}
            onClick={() => handleGroupToggle(groupId)}
          >
            <div className="flex items-center justify-between mb-4">
              <div className="flex items-center">
                <div className="bg-gradient-to-r from-blue-500 to-blue-600 rounded-lg p-3 mr-3">
                  <span className="text-white text-2xl">{group.icon}</span>
                </div>
                <h3 className="font-semibold text-gray-800">{group.name}</h3>
              </div>
              <input
                type="checkbox"
                checked={selectedGroups.includes(groupId)}
                onChange={() => handleGroupToggle(groupId)}
                className="w-5 h-5 text-blue-600 rounded focus:ring-blue-500"
              />
            </div>
            <p className="text-gray-600 text-sm mb-4">{group.description}</p>
            
            {/* 显示示例服务 */}
            <div className="flex flex-wrap gap-2">
              {groupId === 'streaming' && ['Netflix', 'YouTube', 'Spotify', 'Disney+', 'Hulu', 'Prime Video', 'Apple TV+', '+3'].map((service, index) => (
                <span key={index} className="inline-block px-2 py-1 bg-purple-100 text-purple-700 text-xs rounded-full font-medium">
                  {service}
                </span>
              ))}
              {groupId === 'social' && ['Telegram', 'WhatsApp', 'Line', 'Discord', 'Signal', 'WeChat', 'Instagram', '+3'].map((service, index) => (
                <span key={index} className="inline-block px-2 py-1 bg-pink-100 text-pink-700 text-xs rounded-full font-medium">
                  {service}
                </span>
              ))}
              {groupId === 'ai' && ['OpenAI/ChatGPT', 'Claude', 'Bing AI', 'Gemini', 'Perplexity'].map((service, index) => (
                <span key={index} className="inline-block px-2 py-1 bg-indigo-100 text-indigo-700 text-xs rounded-full font-medium">
                  {service}
                </span>
              ))}
              {groupId === 'techgiants' && ['Apple服务', 'Google服务', 'Microsoft服务', 'Amazon服务'].map((service, index) => (
                <span key={index} className="inline-block px-2 py-1 bg-blue-100 text-blue-700 text-xs rounded-full font-medium">
                  {service}
                </span>
              ))}
              {groupId === 'gaming' && ['Steam', 'Epic Games', 'PlayStation', 'Xbox Live', 'Nintendo', 'Battle.net', 'Origin'].map((service, index) => (
                <span key={index} className="inline-block px-2 py-1 bg-red-100 text-red-700 text-xs rounded-full font-medium">
                  {service}
                </span>
              ))}
              {groupId === 'finance' && ['PayPal', '支付宝', 'Stripe', 'Square'].map((service, index) => (
                <span key={index} className="inline-block px-2 py-1 bg-green-100 text-green-700 text-xs rounded-full font-medium">
                  {service}
                </span>
              ))}
              {groupId === 'shopping' && ['Amazon', '淘宝', '京东', 'eBay', 'AliExpress'].map((service, index) => (
                <span key={index} className="inline-block px-2 py-1 bg-yellow-100 text-yellow-700 text-xs rounded-full font-medium">
                  {service}
                </span>
              ))}
              {groupId === 'news' && ['BBC', 'CNN', 'Reuters', 'AP News', 'Bloomberg'].map((service, index) => (
                <span key={index} className="inline-block px-2 py-1 bg-gray-100 text-gray-700 text-xs rounded-full font-medium">
                  {service}
                </span>
              ))}
              {groupId === 'developer' && ['GitHub', 'GitLab', 'Stack Overflow', 'Docker Hub', 'NPM'].map((service, index) => (
                <span key={index} className="inline-block px-2 py-1 bg-teal-100 text-teal-700 text-xs rounded-full font-medium">
                  {service}
                </span>
              ))}
              {groupId === 'adblock' && ['广告拦截', '隐私保护', '劫持防护', '恶意软件防护'].map((service, index) => (
                <span key={index} className="inline-block px-2 py-1 bg-orange-100 text-orange-700 text-xs rounded-full font-medium">
                  {service}
                </span>
              ))}
            </div>
          </div>
        ))}
      </div>

      {/* 选择统计 */}
      <div className="mt-8 bg-white rounded-xl shadow-lg p-6">
        <div className="flex items-center justify-between">
          <div>
            <h3 className="text-lg font-semibold text-gray-800">当前选择</h3>
            <p className="text-gray-600">已选择 {selectedGroups.length} 个策略组</p>
          </div>
          <div className="flex space-x-3">
            <button
              onClick={() => setSelectedGroups(Object.keys(groupTypes))}
              className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors btn-hover"
            >
              全选
            </button>
            <button
              onClick={() => setSelectedGroups([])}
              className="px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition-colors btn-hover"
            >
              清除
            </button>
          </div>
        </div>
      </div>
    </div>
  )

  const renderAboutTab = () => (
    <div className="max-w-4xl mx-auto">
      <div className="text-center mb-8">
        <h2 className="text-3xl font-bold text-gray-800 mb-3">关于程序</h2>
        <p className="text-gray-600 text-lg">功能强大的Clash订阅转换工具</p>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
        <div className="bg-white rounded-xl shadow-lg p-6 card-hover">
          <div className="flex items-center mb-4">
            <div className="bg-gradient-to-r from-blue-500 to-blue-600 rounded-lg p-3 mr-4">
              <span className="text-white text-2xl">📊</span>
            </div>
            <h3 className="text-xl font-semibold text-gray-800">程序信息</h3>
          </div>
          
          <div className="space-y-4">
            {[
              { label: '版本', value: appInfo?.version || 'v2.0', icon: '🏷️' },
              { label: '规则集数量', value: `${appInfo?.total_rulesets || 76}个`, icon: '📦' },
              { label: '策略组类型', value: `${appInfo?.group_types || 10}种`, icon: '🔧' },
              { label: '规则来源', value: appInfo?.rule_source || 'blackmatrix7', icon: '🌐' }
            ].map((item, index) => (
              <div key={index} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                <div className="flex items-center">
                  <span className="text-xl mr-3">{item.icon}</span>
                  <span className="text-gray-600">{item.label}</span>
                </div>
                <span className="font-semibold text-gray-800">{item.value}</span>
              </div>
            ))}
          </div>
        </div>

        <div className="bg-white rounded-xl shadow-lg p-6 card-hover">
          <div className="flex items-center mb-4">
            <div className="bg-gradient-to-r from-green-500 to-green-600 rounded-lg p-3 mr-4">
              <span className="text-white text-2xl">✨</span>
            </div>
            <h3 className="text-xl font-semibold text-gray-800">技术特性</h3>
          </div>
          <div className="space-y-3">
            {(appInfo?.features || [
              '支持多种订阅格式',
              '智能缓存系统',
              '精细分流规则',
              '完善错误处理',
              '响应式Web界面'
            ]).map((feature, index) => (
              <div key={index} className="flex items-center p-3 bg-gray-50 rounded-lg">
                <span className="text-green-500 mr-3 text-xl">✅</span>
                <span className="text-gray-700">{feature}</span>
              </div>
            ))}
          </div>
        </div>
      </div>

      <div className="bg-white rounded-xl shadow-lg p-8">
        <div className="text-center mb-6">
          <div className="bg-gradient-to-r from-purple-500 to-purple-600 rounded-lg p-4 inline-block mb-4">
            <span className="text-white text-3xl">🚀</span>
          </div>
          <h3 className="text-2xl font-semibold text-gray-800 mb-2">开源项目</h3>
          <p className="text-gray-600">
            本项目采用MIT开源许可证，欢迎贡献代码和提出建议。
          </p>
        </div>
        
        <div className="flex justify-center space-x-4">
          <button className="flex items-center px-6 py-3 bg-gray-800 text-white rounded-xl hover:bg-gray-900 transition-all btn-hover shadow-lg">
            <span className="mr-2 text-xl">⭐</span>
            GitHub
          </button>
          <button className="flex items-center px-6 py-3 bg-blue-600 text-white rounded-xl hover:bg-blue-700 transition-all btn-hover shadow-lg">
            <span className="mr-2 text-xl">📖</span>
            文档
          </button>
          <button className="flex items-center px-6 py-3 bg-green-600 text-white rounded-xl hover:bg-green-700 transition-all btn-hover shadow-lg">
            <span className="mr-2 text-xl">💬</span>
            反馈
          </button>
        </div>
      </div>
    </div>
  )

  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
      {/* 头部导航 */}
      <header className="bg-white shadow-lg">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between h-20">
            <div className="flex items-center">
              <div className="flex items-center">
                <div className="bg-gradient-to-r from-blue-600 to-blue-700 rounded-xl p-3 mr-4 shadow-lg">
                  <span className="text-white text-2xl">⚡</span>
                </div>
                <div>
                  <h1 className="text-2xl font-bold text-gray-900">Clash订阅转换程序</h1>
                  <p className="text-sm text-gray-500">在线转换工具 v2.0 - 功能强大，简单易用</p>
                </div>
              </div>
            </div>
            <div className="flex items-center space-x-4">
              <div className="bg-green-100 text-green-800 px-3 py-1 rounded-full text-sm font-medium">
                🌐 在线版本
              </div>
            </div>
          </div>
        </div>
      </header>

      {/* 标签页导航 */}
      <div className="bg-white border-b shadow-sm">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex space-x-8">
            {[
              { id: 'convert', name: '转换配置', icon: '🔄' },
              { id: 'groups', name: '策略组', icon: '📁' },
              { id: 'about', name: '关于', icon: 'ℹ️' }
            ].map((tab) => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`py-4 px-1 border-b-2 font-medium text-sm transition-all ${
                  activeTab === tab.id
                    ? 'border-blue-500 text-blue-600'
                    : 'border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300'
                }`}
              >
                <span className="mr-2">{tab.icon}</span>
                {tab.name}
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* 主要内容 */}
      <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <div className="fade-in">
          {activeTab === 'convert' && renderConvertTab()}
          {activeTab === 'groups' && renderGroupsTab()}
          {activeTab === 'about' && renderAboutTab()}
        </div>
      </main>

      {/* 页脚 */}
      <footer className="bg-white border-t mt-12 shadow-lg">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <div className="text-center">
            <div className="flex justify-center items-center mb-4">
              <div className="bg-gradient-to-r from-blue-600 to-blue-700 rounded-lg p-2 mr-3">
                <span className="text-white text-lg">⚡</span>
              </div>
              <span className="text-lg font-semibold text-gray-800">Clash订阅转换程序</span>
            </div>
            <p className="text-gray-500 text-sm">
              © 2025 Clash订阅转换程序. 本工具仅供学习和研究使用，请遵守当地法律法规。
            </p>
            <div className="mt-4 flex justify-center space-x-6 text-sm text-gray-400">
              <span>MIT开源许可证</span>
              <span>•</span>
              <span>基于blackmatrix7规则集</span>
              <span>•</span>
              <span>支持多种订阅格式</span>
            </div>
          </div>
        </div>
      </footer>
    </div>
  )
}

export default App

