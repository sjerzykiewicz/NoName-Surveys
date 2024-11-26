FROM node:22-alpine

ARG PUBLIC_BACKEND_HOST
ENV PUBLIC_BACKEND_HOST $PUBLIC_BACKEND_HOST

RUN apk add --no-cache rust cargo rustup curl wasm-pack

WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci

COPY . .
RUN npm run build

CMD ["node", "build"]
