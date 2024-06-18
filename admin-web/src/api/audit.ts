// 감사 로그 API

import { request } from './client'

export interface Audit {
  id: number
  created_at: string
}

export async function listAudits(): Promise<Audit[]> {
  return request<Audit[]>('/audits')
}

export async function getAudit(id: number): Promise<Audit> {
  return request<Audit>(`/audits/${id}`)
}
