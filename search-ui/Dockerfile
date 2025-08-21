# Builder
FROM node:22 AS builder

WORKDIR /app

# Copy only package files first for caching
COPY app/package.json app/yarn.lock ./
RUN yarn install --frozen-lockfile

# Copy all source
COPY app/ .

# Build the React app
RUN yarn build

# Runtime
FROM node:22

WORKDIR /app

# Copy build artifacts and server
COPY --from=builder /app/build ./build
COPY --from=builder /app/node_modules ./node_modules
COPY app/proxy.js ./proxy.js

# Install required global tools
RUN yarn global add serve concurrently express @elastic/search-ui-elasticsearch-connector

EXPOSE 3000

ENV NODE_TLS_REJECT_UNAUTHORIZED=0

# Run both frontend and proxy
CMD ["concurrently", "serve -s build -l 3000", "node proxy.js"]
