// 관리자 웹 공통 API 클라이언트

const BASE_URL = import.meta.env.VITE_API_URL

export interface ApiError {
  detail: string
}

export function getToken(): string | null {
  return localStorage.getItem('acme_admin_token')
}

export async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const token = getToken()
  const res = await fetch(`${BASE_URL}${path}`, {
    ...init,
    headers: {
      'Content-Type': 'application/json',
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
      ...init?.headers,
    },
  })
  if (!res.ok) {
    const error: ApiError = await res.json()
    throw new Error(error.detail)
  }
  return res.json() as Promise<T>
}
