# Deployment Guide

This guide explains how to deploy the Medical Chatbot application to **Google Cloud Run**, using the Google Cloud Console (GUI) and preparing for GitHub Actions CI/CD.

---

## 1. Overview

Deployment happens in two phases:

1. Preparing the Google Cloud environment (GUI)
2. Automating deployments with GitHub Actions (CI/CD)

This document covers phase 1.

---

## 2. Create a Google Cloud Project

1. Open the Google Cloud Console: https://console.cloud.google.com  
2. Open the **Project Selector** at the top.  
3. Click **New Project**.  
4. Name it: `medical-chatbot`.  
5. Click **Create**.

---

## 3. Enable Required APIs

Go to **APIs & Services → Library** and enable:

- Cloud Run Admin API  
- Cloud Build API  
- Artifact Registry API  
- IAM Service Account Credentials API  
- Cloud Resource Manager API  

All must show **Enabled**.

---

## 4. Create an Artifact Registry Repository

1. Go to **Artifact Registry**.  
2. Click **Create Repository**.  
3. Configure:

   - **Name:** `cloud-run-source-deploy`  
   - **Format:** Docker  
   - **Region:** `europe-west1`  
   - **Mode:** Standard  

4. Click **Create**.

This is where your Docker images will be stored.

---

## 5. Create a Service Account for CI/CD

1. Go to **IAM & Admin → Service Accounts**.  
2. Click **Create Service Account**.  
3. Name it: `github-actions`.  
4. Click **Create and Continue**.

### Assign these roles:

- Cloud Run Admin  
- Artifact Registry Admin  
- Storage Admin  
- Service Account User  

Click **Done**.

---

## 6. Generate a JSON Key for GitHub Actions

1. Open the `github-actions` service account.  
2. Go to the **Keys** tab.  
3. Click **Add Key → Create new key**.  
4. Choose **JSON**.  
5. Download the file.

You will upload this JSON to GitHub as a secret.

---

## 7. Create a Cloud Run Service

1. Go to **Cloud Run**.  
2. Click **Create Service**.  
3. Choose **Deploy one revision from an existing container image**.  
4. Use a temporary image:  
   `gcr.io/cloudrun/hello`  
5. Name the service: `medical-chatbot`.  
6. Region: `europe-west1`.  
7. Allow unauthenticated access.  
8. Click **Create**.

This creates the service that CI/CD will update.

---

## 8. Add Environment Variables

1. Open your Cloud Run service.  
2. Click **Edit & Deploy New Revision**.  
3. Expand **Variables & Secrets**.  
4. Add:

