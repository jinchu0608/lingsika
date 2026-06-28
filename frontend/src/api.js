/**
 * 摄影展示网站 — 后端 API 接口
 * 所有请求通过 Vite proxy 转发到 Django (localhost:8001)
 */

const BASE = "/api";

async function fetchJSON(url, options = {}) {
  const res = await fetch(`${BASE}${url}`, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });
  if (!res.ok) throw new Error(`API ${res.status}: ${res.statusText}`);
  return res.json();
}

/* ── 封面 ── */

export function getCover() {
  return fetchJSON("/cover/");
}

/* ── 作品 ── */

export function getGalleryItems() {
  return fetchJSON("/gallery-items/");
}

/* ── 作者 ── */

export function getAuthorAvatar() {
  return fetchJSON("/author-avatar/");
}

export function getAuthorInfo() {
  return fetchJSON("/author-info/");
}
