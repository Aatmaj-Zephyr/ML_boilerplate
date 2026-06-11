#!/usr/bin/env bash

set -e

while true; do
    LATEST=$(ls -t telemetry_logs/*.csv 2>/dev/null | head -n 1 || true)

    if [[ -n "$LATEST" ]]; then
        ln -sf "$(basename "$LATEST")" telemetry_logs/index.csv
        break
    fi

    echo "Waiting for telemetry CSV..."
    sleep 1
done

echo "Starting telemetry server..."
python -m http.server 8000 --directory telemetry_logs &
PID_TELEMETRY=$!


echo "All services started"
echo "Telemetry: http://localhost:8000"
echo ""

cleanup() {

echo ""
echo "Stopping all processes..."
kill $PID_TELEMETRY $PID_IMAGES $PID_MAIN
wait
echo "Shutdown complete"
}

trap cleanup SIGINT SIGTERM

wait
