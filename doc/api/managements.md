# 管理者用 API

## 管理者ログイン API

### Requests

```
POST /api/managements/events/{event_id}/signin
```

```javascript
{
    "password": string
}
```

| param    | type   | description        |
| -------- | ------ | ------------------ |
| event_id | string | イベント ID (UUID) |

### Response

#### 成功時

```
200 OK
```

セッションにログイン情報を保存

#### 失敗時

```
401 Unauthorized
```

## イベント登録 API

### Requests

```
POST /api/managements/events
```

```javascript
{
    "name": string,
    "description": string,
    "password": string
    "teams":[{
        "name": string
    }]
}
```

| param        | type   | description        |
| ------------ | ------ | ------------------ |
| name         | string | イベント名         |
| description  | string | イベント概要       |
| password     | string | 管理者用パスワード |
| teams[].name | string | チーム名           |

### Response

#### 成功時

```
200 OK
```

| param           | type   | description  |
| --------------- | ------ | ------------ |
| event_id        | string | イベント ID  |
| name            | string | イベント名   |
| description     | string | イベント概要 |
| teams[].team_id | string | チーム ID    |
| teams[].name    | string | チーム名     |

```javascript
{
    "event_id": string,
    "name": string,
    "description": string,
    "teams":[{
        "team_id": string,
        "name": string
    }]
}
```

#### 失敗時

##### ID が異なる場合

```
404 NotFound
```

##### 値が不適切な場合

```
400 Bad Request
```

## イベント更新 API

### Requests

```
PUT /api/managements/events/{event_id}
```

```javascript
{
    "name": string,
    "description": string,
}
```

| param    | type   | description        |
| -------- | ------ | ------------------ |
| event_id | string | イベント ID (UUID) |

| param       | type   | description  |
| ----------- | ------ | ------------ |
| name        | string | チーム名     |
| description | string | イベント概要 |

### Response

#### 成功時

```
200 OK
```

| param       | type   | description  |
| ----------- | ------ | ------------ |
| name        | string | チーム名     |
| description | string | イベント概要 |

```javascript
{
    "name": string,
    "description": string,
}
```

#### 失敗時

##### ID が異なる場合

```
404 NotFound
```

##### 値が不適切な場合

```
400 Bad Request
```

## イベント取得 API(管理者版)

### Requests

```
PUT /api/managements/events/{event_id}
```

| param    | type   | description        |
| -------- | ------ | ------------------ |
| event_id | string | イベント ID (UUID) |

### Response

#### 成功時

```
200 OK
```

| param           | type   | description  |
| --------------- | ------ | ------------ |
| event_id        | string | イベント ID  |
| name            | string | イベント名   |
| description     | string | イベント概要 |
| teams[].team_id | string | チーム ID    |
| teams[].name    | string | チーム名     |

```javascript
{
    "event_id": string,
    "name": string,
    "description": string,
    "teams":[{
        "team_id": string,
        "name": string
    }]
}
```

#### 失敗時

##### ID が異なる場合

```
404 NotFound
```

##### 値が不適切な場合

```
400 Bad Request
```

## チーム更新 API(管理者版)

### Requests

```
PUT /api/managements/events/{event_id}/teams/{team_id}
```

```javascript
{
    "name":string,
    "progress":number
}
```

| param    | type   | description        |
| -------- | ------ | ------------------ |
| event_id | string | イベント ID (UUID) |
| team_id  | string | チーム ID (UUID)   |

| param    | type   | description |
| -------- | ------ | ----------- |
| name     | string | イベント名  |
| progress | number | 進捗        |

### Response

#### 成功時

```
200 OK
```

| param    | type   | description |
| -------- | ------ | ----------- |
| name     | string | イベント名  |
| progress | number | 進捗        |

```javascript
{
    "name":string,
    "progress":number
}
```

#### 失敗時

##### ID が異なる場合

```
404 NotFound
```

##### 値が不適切な場合

```
400 Bad Request
```

## チーム追加 API

### Requests

```
POST /api/managements/events/{event_id}/teams
```

```javascript
{
    "name":string,
}
```

| param    | type   | description        |
| -------- | ------ | ------------------ |
| event_id | string | イベント ID (UUID) |

| param | type   | description |
| ----- | ------ | ----------- |
| name  | string | イベント名  |

### Response

#### 成功時

```
200 OK
```

| param    | type   | description |
| -------- | ------ | ----------- |
| name     | string | イベント名  |
| progress | number | 進捗        |

```javascript
{
    "name":string,
    "progress":number
}
```

#### 失敗時

##### ID が異なる場合

```
404 NotFound
```

##### 値が不適切な場合

```
400 Bad Request
```

## チーム削除 API

### Requests

```
 DELETE /api/managements/events/{event_id}/teams/{team_id}
```

| param    | type   | description        |
| -------- | ------ | ------------------ |
| event_id | string | イベント ID (UUID) |
| team_id  | string | チーム ID (UUID)   |

### Response

#### 成功時

```
204 NoContent
```

#### 失敗時

##### ID が異なる場合

```
404 NotFound
```

##### 値が不適切な場合

```
400 Bad Request
```
