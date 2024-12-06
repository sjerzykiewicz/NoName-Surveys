# NoName Anonymous Surveys API
This is the API for the NoName Anonymous Surveys project.

## Version: 1.0.0

### /answers/fetch

#### POST
##### Summary:

Get Survey Answers By Code

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Fetch answers to a given survey |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /answers/fill

#### POST
##### Summary:

Save Survey Answer

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Fill out a survey |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /survey-drafts/all/{page}

#### POST
##### Summary:

Get Survey Drafts

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| page | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Get all Survey Drafts Headers of a user |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /survey-drafts/fetch

#### POST
##### Summary:

Get Survey Draft

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Fetch a survey draft by id |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /survey-drafts/delete

#### POST
##### Summary:

Delete Survey Drafts

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Delete a survey draft |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /survey-drafts/create

#### POST
##### Summary:

Create Survey Draft

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Create a new SurveyStructure Draft |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /survey-drafts/count

#### POST
##### Summary:

Count Survey Drafts

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Number of survey drafts of a user |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /surveys/count

#### POST
##### Summary:

Count Surveys

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Number of surveys of a user |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /surveys/all/{page}

#### POST
##### Summary:

Get Surveys For User

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| page | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Get all survey headers of a user |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /surveys/fetch

#### POST
##### Summary:

Get Survey By Code

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Fetch a survey to fill it out |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /surveys/respondents-count

#### POST
##### Summary:

Count Survey Respondents

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Number of possible respondents for a surveys |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /surveys/respondents/{page}

#### POST
##### Summary:

Get Respondents By Code

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| page | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Get emails of respondents |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /surveys/delete

#### POST
##### Summary:

Delete Surveys

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Delete a survey |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /surveys/create

#### POST
##### Summary:

Create Survey

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Create a new survey |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /surveys/give-access

#### POST
##### Summary:

Give Access To Surveys

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Give access to a survey to other users |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /surveys/take-away-access

#### POST
##### Summary:

Take Away Access To Surveys

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Take away access to a survey from another user |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /surveys/reject-access

#### POST
##### Summary:

Reject Access To Surveys

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Reject access to surveys given by another user |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /surveys/all-with-access-count

#### POST
##### Summary:

Get Count Of Users With Access

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Number of users who can view results of a survey |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /surveys/all-without-access

#### POST
##### Summary:

Get All Users Without Access

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Users who do not have access to a survey |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /surveys/get-all-with-access/{page}

#### POST
##### Summary:

Check Access To Surveys

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| page | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Check who has access to results of a given survey |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /user-groups/count

#### POST
##### Summary:

Get User Groups Count

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Number of all user groups of a given user |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /user-groups/all/{page}

#### POST
##### Summary:

Get User Groups

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| page | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | List of of all user groups of a given user |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /user-groups/all-with-public-keys

#### POST
##### Summary:

Get User Groups With Members Having Public Keys

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | List of names of all user groups of a given user which members all have public keys |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /user-groups/group-members-count

#### POST
##### Summary:

Get User Group Members Count

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Number of members in a given user group |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /user-groups/all-who-are-not-members

#### POST
##### Summary:

Get Users Who Are Not Members

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | List of users who are not members of a given user group |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /user-groups/fetch

#### POST
##### Summary:

Get Whole User Group

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | List of all user emails in a given user group |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /user-groups/fetch/{page}

#### POST
##### Summary:

Get User Group

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| page | path |  | Yes | integer |

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | List of user emails in a given user group |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /user-groups/create

#### POST
##### Summary:

Create User Group

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Create a user group |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /user-groups/rename

#### POST
##### Summary:

Rename User Group

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Rename a user group name |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /user-groups/delete

#### POST
##### Summary:

Delete User Groups

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Delete user groups |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /user-groups/add-users

#### POST
##### Summary:

Add Users To Group

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Add users to a group |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /user-groups/remove-users

#### POST
##### Summary:

Remove Users From Group

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Remove users from a group |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /users/all

#### GET
##### Summary:

Get Users

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | List of all active user emails |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /users/all-with-public-keys

#### GET
##### Summary:

Get Users With Keys

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | List of all active user emails with public key |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /users/validate

#### POST
##### Summary:

Does User Exist

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Validate a user |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /users/has-public-key

#### POST
##### Summary:

Check If User Has Public Key

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Check if user has a non-empty public key |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /users/key-creation-date

#### POST
##### Summary:

Get Key Creation Date

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Get the time of key creation |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /users/register

#### POST
##### Summary:

Create User

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Register a new user |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /users/update-public-key

#### POST
##### Summary:

Update User Public Key

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Update user's public key |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /users/filter-unregistered-users

#### POST
##### Summary:

Filter Unregistered Users

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Returns a list of user emails that are not registered |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |

### /users/filter-users-with-no-public-key

#### POST
##### Summary:

Filter Users With No Public Keys

##### Responses

| Code | Description |
| ---- | ----------- |
| 200 | Returns a list of user emails that have no public key |
| 422 | Validation Error |

##### Security

| Security Schema | Scopes |
| --- | --- |
| HTTPBearer | |
