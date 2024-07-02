// 감사 로그 목록 화면

import { useEffect, useState } from 'react'

import { listAudits, type Audit } from '../api/audit'

export default function AuditListPage() {
  const [items, setItems] = useState<Audit[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    listAudits()
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
