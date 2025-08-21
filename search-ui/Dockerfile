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

# Copy build artifacts only
COPY --from=builder /app/build ./build

# Serve static files
RUN yarn global add serve

EXPOSE 3000
CMD ["serve", "-s", "build", "-l", "3000"]
