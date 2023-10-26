// 쿠폰 API

import { request } from './client'

export interface Coupon {
  id: number
  created_at: string
}

export async function listCoupons(): Promise<Coupon[]> {
  return request<Coupon[]>('/coupons')
}

export async function getCoupon(id: number): Promise<Coupon> {
  return request<Coupon>(`/coupons/${id}`)
}
