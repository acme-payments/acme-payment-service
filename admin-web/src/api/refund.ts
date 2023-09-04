// 환불 API

import { request } from './client'

export interface Refund {
  id: number
  created_at: string
}

export async function listRefunds(): Promise<Refund[]> {
  return request<Refund[]>('/refunds')
}

export async function getRefund(id: number): Promise<Refund> {
  return request<Refund>(`/refunds/${id}`)
}
