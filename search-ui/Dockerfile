# Builder
FROM node:22 AS builder

WORKDIR /app

# Copy only package files first for caching
COPY app/package*.json ./
RUN npm install

# Copy all source
COPY app/ .

# Build the React app
RUN npm run build

# Runtime
FROM node:22

WORKDIR /app

# Copy build artifacts only
COPY --from=builder /app/build ./build

# Serve static files
RUN npm install -g serve

EXPOSE 3000
CMD ["serve", "-s", "build", "-l", "3000"]
