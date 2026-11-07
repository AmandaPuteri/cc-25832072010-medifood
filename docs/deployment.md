# Manual Deployment M03

- Path aplikasi: /srv/cc-m03
- Service: cc-m03.service
- Backend: 127.0.0.1:8000
- Endpoint publik: http://<PUBLIC_IP>/

## Prosedur Update

```bash
cd /srv/cc-m03
git pull
source .venv/bin/activate
python -m pip install -r requirements.txt
sudo systemctl restart cc-m03
curl -fsS http://127.0.0.1/health
```
