# NoName Anonymous Surveys

**NoName Anonymous Surveys** is an open-source platform designed for conducting truly anonymous surveys. Using linkable ring signature technology, it ensures that:

#### - ✅ Responses are verifiable as being from members of a designated group.
#### - ✅ Respondent identities remain entirely anonymous.
#### - ✅ Each user can respond only once to a survey.

You are free to use, modify, and host your own instance of the platform. Setup instructions and tips are provided below.

---

## 🎯 Key Features
1. **Anonymity**: Identity protection through cryptographic techniques.
2. **Group-Specific Access**: Surveys can be restricted to specific groups or open to the public.
3. **User-Friendly**: Easy setup and usage for both users and administrators.

---

## 🚀 Example Use Case

### Check out the example instance for the **University of Adam Mickiewicz** [here](https://nonamesurveys.projektstudencki.pl/).
> [!NOTE]
> Keep in mind that this instance can be accessed only by students and staff of the university.

---

## 📖 User's Guide

> [!IMPORTANT]
> The keys used in the cryptographic protocol are generated locally on your device.
> **Do not lose your keys** – they are required for you to answer private surveys.

### 1️⃣ **Generate Keys**
Your cryptographic keys are generated **locally on your device**, ensuring your private key never leaves your hands.
1. Go to the **Account** section in the navigation bar.
2. Enter a **passphrase** (used to encrypt and decrypt your keys) and confirm it.
3. Click on **Generate Keys**.
4. Save the keys in a secure location.

---

### 2️⃣ **Create a Survey**
1. Navigate to the **Create** section in the navigation bar.
2. Fill out the survey title and questions.
3. Optionally:
   - Save a draft for later use by clicking **Save Draft**.
   - Preview the survey by clicking **Preview**.
4. Once ready, click **Finish**.
5. Choose who can respond to the survey:
   - **Secure** (restricted to specific users or groups):
     - Select a user group from the list or add users by email.
     - Ensure all users have registered and generated their keys.
   - **Public** (open to everyone).
6. Click **Finish** again to finalize.

---

### 3️⃣ **Respond to a Survey**
1. Open the survey link.
2. Fill out the form with your responses.
3. If the survey has a restricted access, you will be asked to **load your keys** and **enter the passphrase** you have generated during keys creation.
4. Click **Submit**.

---

### 4️⃣ **View Survey Results**
1. Navigate to the **Surveys** section in the navigation bar.
2. Click on the survey you are interested in.
3. You will see the summary of responses but will be able to see individual responses if you nagivate to the **Answers** tab.

---

### 5️⃣ **Create a User Group**
1. Navigate to the **Groups** section in the navigation bar.
2. Click on the **+ Group** button.
3. Fill out the group name.
4. Add users by email or import them from a CSV file.
5. Click **Submit**.

---

## 🛠 Administrator's Guide

### 1️⃣ **Dependencies**
- **Node.js (npm)**
- **Python**

---

### 2️⃣ **Setup**
You can deploy the app using Docker images or build it locally.

#### Using Prebuilt Docker Images:
```bash
docker compose up
