# イベント API

## イベント情報取得 API

### Requests

```
GET /api/events/{event_id}
```

| param    | type   | description        |
| -------- | ------ | ------------------ |
| event_id | string | イベント ID (UUID) |

### Response

#### 成功時

```
200 OK
```

| param       | type   | description |
| ----------- | ------ | ----------- |
| name        | string | イベント名  |
| description | string | 説明        |

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

## チーム情報一覧取得 API

### Requests

```
GET /api/events/{event_id}/teams
```

| param    | type   | description        |
| -------- | ------ | ------------------ |
| event_id | string | イベント ID (UUID) |

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
    "teams": [{
        "name":string,
        "progress":number
    }]
}
```

#### 失敗時

##### ID が異なる場合

```
404 NotFound
```

## チーム詳細取得 API

### Requests

```
GET /api/events/{event_id}/teams/{team_id}
```

| param    | type   | description        |
| -------- | ------ | ------------------ |
| event_id | string | イベント ID (UUID) |
| team_id  | string | チーム ID (UUID)   |

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

## チーム進捗更新 API

### Requests

```
PUT /api/events/{event_id}/teams/{team_id}/progress
```

```javascript
{
    "progress": number
}
```

| param    | type   | description        |
| -------- | ------ | ------------------ |
| event_id | string | イベント ID (UUID) |
| team_id  | string | チーム ID (UUID)   |

| param    | type   | description |
| -------- | ------ | ----------- |
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

##### 進捗の値が誤っている場合

```
400 Bad Request
```

## チーム名更新 API

### Requests

```
PUT /api/events/{event_id}/teams/{team_id}/name
```

```javascript
{
    "name": string
}
```

| param    | type   | description        |
| -------- | ------ | ------------------ |
| event_id | string | イベント ID (UUID) |
| team_id  | string | チーム ID (UUID)   |

| param | type   | description |
| ----- | ------ | ----------- |
| name  | string | チーム名    |

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

##### 名前が不適切な場合(文字数オーバー等)

```
400 Bad Request
```
