TEST_SURVEY_STRUCTURE = {
    "questions": [
        {
            "question_type": "binary",
            "required": True,
            "question": "Is this a test?",
            "choices": ["Yes", "No"]
        },
        {
            "question_type": "list",
            "required": True,
            "question": "Is this a test?",
            "choices": ["Yes", "No"]
        },
        {
            "question_type": "multi",
            "required": True,
            "question": "Is this a test?",
            "choices": ["Yes", "No"]
        },
        {
            "question_type": "number",
            "required": True,
            "question": "Is this a test?",
            "min_value": 0,
            "max_value": 10
        },
        {
            "question_type": "rank",
            "required": True,
            "question": "Is this a test?",
            "choices": ["Yes", "No"]
        },
        {
            "question_type": "scale",
            "required": True,
            "question": "Is this a test?"
        },
        {
            "question_type": "single",
            "required": True,
            "question": "Is this a test?",
            "choices": ["Yes", "No"]
        },
        {
            "question_type": "slider",
            "required": True,
            "question": "Is this a test?",
            "min_value": 0,
            "max_value": 10
        },
        {
            "question_type": "text",
            "required": True,
            "question": "Is this a test?",
            "details": "details"
        },
        {
            "subtitle": "This test section covers..."
        }
    ]
}

TEST_PUBLIC_KEY_1 = "".join(
    (
        "-----BEGIN PUBLIC KEY-----\n",
        "MTcwNDAzNTg4MzkyMjE3NTU2MDQyMjE4MDk2MDMwMDc1MzcxMzUxODM1NjI4Mzgz\n",
        "MDIwNTU3MTM0ODkwMTIyNzQ2MTQ3NTg1NzM1OTg5Mzk3MTI3MDc0OTc0Njk1MDIy\n",
        "NTUyODkxMTE0NzUwMjA1OTcxMDg3ODgwODY0MjU3NzI4OTk4MTIzOTU4OTA5MzE4\n",
        "ODg0NDQ3MDM2MzY0Mzg3MjY3Mjk0MzIzMzIzMTM1MzAxODY1MTUyNDk2ODAwNDA1\n",
        "MzM4ODk5MDg3NTk3MTk3OTc2OTkwMzc3ODg4NzQ0MjQyODQwMTUzNTU2NzM2ODg4\n",
        "MTQxMDc0NzIwNzYwNjg2ODU1MzA5MDk0MTkwMDU3MzMwOTAxNTI1ODI1NDE5MTY4\n",
        "NDQwNzIxOTQ3NzE0MjIyNzQ5OTUyMTYxNjA0MDQ4NTgwNzIyNzYxODAxMTk3MjI0\n",
        "Mjg3MDU1NDQ0MTg5MTI2MzQyMTE5MTc0MTA0MTg5NDgxODA5NTk3MTYyMTUyMTIy\n",
        "MDczODEyNTM3MTk3MzA5NzQ0MTUzNTYzNjEwODUwNjg4Mzg2NDQ2NzQ2MDQwMTI3\n",
        "MDcxMjE2NjQ2OTQxMDYxNzUxMzQ0MDQ2ODU5OTkxNjYwNDgzOTE3MDA1OTUxNDQ2\n",
        "OTc3MTM0MjY1ODUwNjcwMTAzMzgyMDQ4NDI2NjYxMzc3MDAyMTY5MDk2Mjg2ODAy\n",
        "NTg2NTcyMDE1MzIzMjY4NzMyMTQwMjEwMjkwMTkxODU2MjI0MDAwMjU3ODIxNzg2\n",
        "OTEyNTI0NzM3MjI5NDU2Mzg5NTYxNTc0MjE2MjgzNzE2NTc2NjM0NTU=\n",
        "-----END PUBLIC KEY-----"
    )
)

TEST_PUBLIC_KEY_2 = "".join(
    (
        "-----BEGIN PUBLIC KEY-----\n",
        "MTUxNzQ0OTMxOTkzNTkwNjc0NTIzODA3OTk3NzcyODMzNzg4NDU1Mjg2ODM3Mzk4\n",
        "NTE4NDA5ODI5MDc3OTM1MjY2MDIxMTI3ODY4MzcyMDU3NTMwOTAyNTgxNDIyODUz\n",
        "NTU1NzkxNzUyODc0OTExMjI2NTU3MjIzNTgxMjU1MzUwMzA5MDA1NzYwMDE3NDk1\n",
        "MjQ3NDY4OTg0OTkzMTU1ODkzNDM5MTMzMTQxNTgzNTYyNDE3NzA1ODYwODQzMzcy\n",
        "ODg4MzQyNDU0Njc4NjIyOTAzNDYyOTcxNjIwMDQxMTE5MTg5NDI1MzUxNzkyODEx\n",
        "ODQzMDE3NzYwMTI5MzAwNjA4NTExNDEzMTI0MTQ2Nzc0MzAyNTI0OTY4NTY5MjYx\n",
        "MTQ0Njc4NjQ4Njg4MjkzNzA5Njg4NjM3MTIyMjUyNTI4NzYxNDgyMTgwMDY4ODE1\n",
        "MzMzNzc3ODY2OTE2NjkwNzc5NTgzODQ1OTE0MjM1ODkzOTg5NDQxMzE3NjA2NTQx\n",
        "NDA4OTQ4MTI3NzU1MDEzMjUzMzUyNzg3NzU4OTU2OTk3Mjg0MDU0ODAzMDgxMzY4\n",
        "ODE3MTEyNDIwOTEzNTM4MDE3NzI0NDI1OTY4NjQxMDIyMTk4NzY0NzY2NjU4ODE5\n",
        "MDAwODgzNTU0NzUyMTAxMjM1MTIyODE2OTk3MDg2MTYxOTE1NDQyNTQ3MzA1NjU5\n",
        "OTAzMDAyMDA1NzU4NDk1MTEwNjA0NTU1NTUxMzAyMDEwMTU0ODI0NjMzMzkyMjQy\n",
        "MjUxMDI2OTg5NDk5NDI4MTk4MDI3NTk3OTkxMjUxMjE4MDc2ODk3Nzk=\n",
        "-----END PUBLIC KEY-----"
    )
)

TEST_ZERO_AS_PUBLIC_KEY = ("-----BEGIN PUBLIC KEY-----\nMA==\n-----END PUBLIC KEY-----")

TEST_INCORRECT_PUBLIC_KEY = "".join(
    (
        "-----BEGIN PUBLIC KEY-----\n",
        "MTUxNzQ0OTMxOTkzNTkwNjc0NTIzODA3OTk3NzcyODMzNzg4NDU1Mjg2ODM3Mzk4\n",
        "-----END PUBLIC KEY-----"
    )
)
