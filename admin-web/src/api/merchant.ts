// 가맹점 API

import { request } from './client'

export interface Merchant {
  id: number
  created_at: string
}

export async function listMerchants(): Promise<Merchant[]> {
  return request<Merchant[]>('/merchants')
}

export async function getMerchant(id: number): Promise<Merchant> {
  return request<Merchant>(`/merchants/${id}`)
}
