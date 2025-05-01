#!/bin/bash
set -e

if [ -z "$CRON" ]; then
  echo "Error: CRON environment variable not set"
  exit 1
fi

echo "Setting up cron job with schedule: '$CRON'"

# Write the cron schedule to a crontab file
echo "$CRON /usr/local/bin/autoremove-torrents --conf /app/config.yml >> /var/log/cron.log 2>&1" > /etc/cron.d/autoremove-cron

# Apply correct permissions
chmod 0644 /etc/cron.d/autoremove-cron

# Register the new cron job
crontab /etc/cron.d/autoremove-cron

# Create the log file
touch /var/log/cron.log

# Start cron in foreground
cron && tail -f /var/log/cron.log
