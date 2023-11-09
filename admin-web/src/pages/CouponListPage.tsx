// 쿠폰 목록 화면

import { useEffect, useState } from 'react'

import { listCoupons, type Coupon } from '../api/coupon'

export default function CouponListPage() {
  const [items, setItems] = useState<Coupon[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    listCoupons()
      .then(setItems)
      .finally(() => setLoading(false))
  }, [])

  if (loading) return <p>불러오는 중…</p>

  return (
    <table>
      <tbody>
        {items.map((item) => (
          <tr key={item.id}>
            <td>{item.id}</td>
            <td>{item.created_at}</td>
          </tr>
        ))}
      </tbody>
    </table>
  )
}
