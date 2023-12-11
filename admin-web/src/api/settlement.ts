// 정산 API

import { request } from './client'

export interface Settlement {
  id: number
  created_at: string
}

export async function listSettlements(): Promise<Settlement[]> {
  return request<Settlement[]>('/settlements')
}

export async function getSettlement(id: number): Promise<Settlement> {
  return request<Settlement>(`/settlements/${id}`)
}
