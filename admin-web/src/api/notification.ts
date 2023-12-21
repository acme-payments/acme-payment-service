// 알림 API

import { request } from './client'

export interface Notification {
  id: number
  created_at: string
}

export async function listNotifications(): Promise<Notification[]> {
  return request<Notification[]>('/notifications')
}

export async function getNotification(id: number): Promise<Notification> {
  return request<Notification>(`/notifications/${id}`)
}
