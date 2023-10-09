// 환불 목록 화면

import { useEffect, useState } from 'react'

import { listRefunds, type Refund } from '../api/refund'

export default function RefundListPage() {
  const [items, setItems] = useState<Refund[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    listRefunds()
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
