// 구독 API

import { request } from './client'

export interface Subscription {
  id: number
  created_at: string
}

export async function listSubscriptions(): Promise<Subscription[]> {
  return request<Subscription[]>('/subscriptions')
}

export async function getSubscription(id: number): Promise<Subscription> {
  return request<Subscription>(`/subscriptions/${id}`)
}
