import { IonApp, IonHeader, IonToolbar, IonTitle, IonContent, IonItem, IonLabel, IonInput, IonList, IonCheckbox, IonButton, IonAlert, IonLoading } from '@ionic/react';
import { useEffect, useState } from 'react';

// 通过环境变量 VITE_API_BASE_URL 指定后端地址，默认指向同源的 /api
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || '/api';

function App() {
  const [subscriptionUrl, setSubscriptionUrl] = useState('');
  const [groupTypes, setGroupTypes] = useState({});
  const [selected, setSelected] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    fetch(`${API_BASE_URL}/groups`)
      .then(res => res.json())
      .then(data => {
        if (data.success) {
          setGroupTypes(data.groups);
        }
      })
      .catch(() => {});
  }, []);

  const toggle = (id) => {
    setSelected(prev => prev.includes(id) ? prev.filter(x => x !== id) : [...prev, id]);
  };

  const handleConvert = async () => {
    if (!subscriptionUrl.trim()) return;
    setIsLoading(true);
    setError('');
    try {
      const res = await fetch(`${API_BASE_URL}/convert`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ subscription_url: subscriptionUrl, selected_groups: selected })
      });
      const data = await res.json();
      if (data.success) {
        setResult(data);
      } else {
        setError(data.error || '转换失败');
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  const downloadConfig = () => {
    if (!result) return;
    const blob = new Blob([result.config_content], { type: 'text/yaml' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = result.filename || 'clash_config.yaml';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  return (
    <IonApp>
      <IonHeader>
        <IonToolbar color="primary">
          <IonTitle>Clash Converter</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent className="ion-padding">
        <IonItem>
          <IonLabel position="stacked">订阅链接</IonLabel>
          <IonInput value={subscriptionUrl} onIonChange={e => setSubscriptionUrl(e.detail.value)} placeholder="https://example.com/sub" />
        </IonItem>
        <IonList>
          {Object.entries(groupTypes).map(([id, g]) => (
            <IonItem key={id} lines="none">
              <IonLabel>{g.name}</IonLabel>
              <IonCheckbox slot="end" checked={selected.includes(id)} onIonChange={() => toggle(id)} />
            </IonItem>
          ))}
        </IonList>
        <IonButton expand="block" onClick={handleConvert}>开始转换</IonButton>
        <IonButton expand="block" color="medium" onClick={downloadConfig} disabled={!result}>下载配置文件</IonButton>
        <IonAlert isOpen={!!error} onDidDismiss={() => setError('')} header="错误" message={error} buttons={['OK']} />
        <IonLoading isOpen={isLoading} message="转换中..." />
      </IonContent>
    </IonApp>
  );
}

export default App;
