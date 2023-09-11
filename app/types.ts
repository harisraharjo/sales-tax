import type { InputSeparator } from "./constants"

type BaseType = {
  id: number
  name: string
}

export type TaxType = BaseType

export type EntriesProps = {
  taxes: { id: number; name: string }[]
  kinds: { id: number; name: string }[]
  measurements: { id: number; name: string }[]
}

export type EntriesOutput = {
  prices: number[]
  total_tax: number
  total_price: number
}

export type InputDisplayText = `${string}${InputSeparator}${string}`

export const entriesOutputKeys = [
  "amount",
  "measurement_type",
  "tax_type",
  "product_name",
  "product_type",
  "price",
] as const

export type Keys = typeof entriesOutputKeys
