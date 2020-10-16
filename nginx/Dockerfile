# Use the nginx image
FROM nginx

# Remove the default pre-set that nginx comes with
RUN rm /etc/nginx/conf.d/default.conf

# Replace the previous pre-set with our own tailored one
COPY nginx.conf /etc/nginx/conf.d/