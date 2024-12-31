#! /bin/bash
curl -X POST -H 'Content-Type: application/json' -d '{"user_email": "test@test.com"}' http://localhost:8000/users/register
response=$(curl -X POST -H 'Content-Type: application/json' -d '{"user_email": "test@test.com", "title":"test","survey_structure":{"questions":[{"required":false,"question":"test","question_type":"text","details":""}]},"uses_cryptographic_module":false,"ring_members":[]}' http://localhost:8000/surveys/create)
survey_code=$(echo $response | jq -r '.survey_code')
export SURVEY_CODE=$survey_code
echo "Survey code saved to environment variable: $SURVEY_CODE"
