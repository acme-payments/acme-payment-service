// 이의제기 API

import { request } from './client'

export interface Dispute {
  id: number
  created_at: string
}

export async function listDisputes(): Promise<Dispute[]> {
  return request<Dispute[]>('/disputes')
}

export async function getDispute(id: number): Promise<Dispute> {
  return request<Dispute>(`/disputes/${id}`)
}
