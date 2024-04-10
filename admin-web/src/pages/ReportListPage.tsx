// 리포트 목록 화면

import { useEffect, useState } from 'react'

import { listReports, type Report } from '../api/report'

export default function ReportListPage() {
  const [items, setItems] = useState<Report[]>([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    listReports()
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
