# DB Document

## Events

| param       | type         | option   |
| ----------- | ------------ | -------- |
| id          | BIGINT       | pk       |
| name        | VARCHAR(45)  | NOT NULL |
| description | VARCHAR(200) | NOT NULL |
| passwd      | VARCHAR(45)  | NOT NULL |

## Teams

| param    | type        | option   |
| -------- | ----------- | -------- |
| id       | BIGINT      | pk       |
| event_id | BIGINT      | fk       |
| name     | VARCHAR(45) | NOT NULL |
| progress | INT         | NOT NULL |
