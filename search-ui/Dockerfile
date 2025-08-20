FROM node:22-alpine AS builder

WORKDIR /app

COPY app/package*.json ./

RUN npm install

COPY app/ .

RUN npm run build


FROM nginx:alpine

COPY --from=builder /app/build /usr/share/nginx/html

EXPOSE 3000

ENTRYPOINT ["nginx", "-g", "daemon off;"]
