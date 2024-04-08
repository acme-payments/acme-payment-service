// 리포트 API

import { request } from './client'

export interface Report {
  id: number
  created_at: string
}

export async function listReports(): Promise<Report[]> {
  return request<Report[]>('/reports')
}

export async function getReport(id: number): Promise<Report> {
  return request<Report>(`/reports/${id}`)
}
