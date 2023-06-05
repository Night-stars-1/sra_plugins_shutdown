<div align="center">

<h1>星穹铁道小助手消息推送插件</h1>
  
</div>

## 使用方法
  * 将`sra_plugins_notify`放置在StarRailAssistant的`plugins`目录下载

### 配置推送：
- 推送名称 / notifier: bark

  参数大全 / params:
  {'required': ['key'], 'optional': ['title', 'sound', 'isarchive', 'icon', 'group', 'url', 'copy', 'autocopy']}

- 推送名称 / notifier: custom

  参数大全 / params:
  {'required': ['url'], 'optional': ['method', 'datatype', 'data']}

- 推送名称 / notifier: dingtalk

  参数大全 / params:
  {'required': ['token'], 'optional': ['title', 'secret', 'markdown']}

- 推送名称 / notifier: discord

  参数大全 / params:
  {'required': ['webhook'], 'optional': ['title', 'username', 'avatar_url', 'color']}

- 推送名称 / notifier: pushplus

  参数大全 / params:
  {'required': ['token'], 'optional': ['title', 'topic', 'markdown']}

- 推送名称 / notifier: qmsg

  参数大全 / params:
  {'required': ['key'], 'optional': ['title', 'mode', 'qq']}

- 推送名称 / notifier: serverchan

  参数大全 / params:
  {'required': ['sckey', 'title'], 'optional': []}

- 推送名称 / notifier: serverchanturbo

  参数大全 / params:
  {'required': ['sctkey', 'title'], 'optional': ['channel', 'openid']}

- 推送名称 / notifier: telegram

  参数大全 / params:
  {'required': ['token', 'userid'], 'optional': ['title', 'api_url']}

- 推送名称 / notifier: wechatworkapp

  参数大全 / params:
  {'required': ['corpid', 'corpsecret', 'agentid'], 'optional': ['title', 'touser', 'markdown']}

- 推送名称 / notifier: wechatworkbot

  参数大全 / params:
  {'required': ['key'], 'optional': ['title', 'markdown']}
* **required为必填参数，optional为选填参数**

配置参考：
```json
"ONEPUSH": {
  "notifier": "telegram",
  "params": {
    "title": "",
    "markdown": false,
    "token": "xxxxxxxxx:xxxxxxxxxxxxxxxxxxxxx",
    "userid": 123456789
  }
}
```
```json
"ONEPUSH": {
  "notifier": "pushplus",
  "params": {
    "title": "",
    "token": "XXXXXXXXXXXXXXXXXXXXXXXX",
    "markdown": false
  }
}
```

完整配置参考
```json
{
  "real_width": 0,
  "auto_battle_persistence": 0,
  "real_height": 0,
  "github_proxy": "",
  "rawgithub_proxy": "",
  "webhook_url": "",
  "start": true,
  "temp_version": "0",
  "star_version": "0",
  "open_map": "m",
  "level": "INFO",
  "adb": "127.0.0.1:7555",
  "adb_path": "temp\\adb\\adb",
  "proxies": "",
  "scaling": 1.0,
  "borderless": true,
  "map_version": "0",
  "ONEPUSH": {
    "notifier": "telegram",
    "params": {
      "title": "",
      "markdown": false,
      "token": "xxxxxxxxx:xxxxxxxxxxxxxxxxxxxxx",
      "userid": 123456789
    }
  }
}
```