import http from 'k6/http';
import { check } from 'k6';

export const options = { vus: 30, duration: '30s' };

export default function () {
  const path = __ENV.ENDPOINT || 'fast';
  const res = http.get(`http://localhost:5000/${path}`);
  check(res, { 'status 200 байна': (r) => r.status === 200 });
}
