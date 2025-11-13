FROM node:22-alpine3.20 AS build

WORKDIR /app

RUN apk add --no-cache python3 make g++

COPY package*.json ./

RUN npm ci --production=false

COPY . .

RUN npm run build && \
    rm -rf node_modules && \
    npm ci --production

FROM nginx:1.27-alpine

RUN apk add --no-cache ca-certificates tzdata

COPY --from=build /app/dist /usr/share/nginx/html

COPY nginx.conf /etc/nginx/conf.d/default.conf

RUN chmod -R 755 /usr/share/nginx/html

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]
