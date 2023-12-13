// 정산 목록 화면

import { useEffect, useState } from 'react'

import { listSettlements, type Settlement } from '../api/settlement'

export default function SettlementListPage() {
  const [items, setItems] = useState<Settlement[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    listSettlements()
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
