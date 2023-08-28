// 로그인·토큰 처리

import { request } from './client'

export interface LoginResponse {
  access_token: string
}

export async function login(email: string, password: string): Promise<LoginResponse> {
  return request<LoginResponse>('/auth/login', {
    method: 'POST',
    body: JSON.stringify({ email, password }),
  })
}

export async function logout(): Promise<void> {
  localStorage.removeItem('acme_admin_token')
}
