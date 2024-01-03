// 웹훅 API

import { request } from './client'

export interface Webhook {
  id: number
  created_at: string
}

export async function listWebhooks(): Promise<Webhook[]> {
  return request<Webhook[]>('/webhooks')
}

export async function getWebhook(id: number): Promise<Webhook> {
  return request<Webhook>(`/webhooks/${id}`)
}
