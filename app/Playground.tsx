import { PropsWithChildren } from "react"
import { entriesOutputKeys, Keys } from "./types"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import { Combobox } from "@/components/ui/combobox"
import { SendHorizonal } from "lucide-react"
import { revalidatePath } from "next/cache"
import {
  VALUE_SEPARATOR,
  POST_SEPARATOR,
  SPACE,
  INPUT_SEPARATOR,
  OUTPUT_SEPARATOR,
  OUTPUT_TOTAL_TAX,
  OUTPUT_TOTAL_PRICE,
} from "./constants"
import { postJSON } from "@/lib/utils"
import type { EntriesOutput, EntriesProps, InputDisplayText } from "./types"
import { Separator } from "@/components/ui/separator"

type Enumerate<
  N extends number,
  Acc extends number[] = [],
> = Acc["length"] extends N
  ? Acc[number]
  : Enumerate<N, [...Acc, Acc["length"]]>

type Range<F extends number, T extends number> = Exclude<
  Enumerate<T>,
  Enumerate<F>
>
export type RawIdx = Range<0, RawData["length"]>

type Amount = number
type Measurement = number
type Name = string
type ProductType = number
type TradeType = number
export type RawData = [Amount, Measurement, Name, ProductType, TradeType]

const INPUT_TITLE = "Input"

const OUTPUT_TITLE = "Output"

type InputData = {
  value: string
  label: InputDisplayText
}
const inputDisplay: InputData[] = []

type OutputSeparator = typeof OUTPUT_SEPARATOR
type Space = typeof SPACE
type OutputDisplayText =
  | `${string}${OutputSeparator}${Space}${string}`
  | `${typeof OUTPUT_TOTAL_TAX}${OutputSeparator}${Space}${string}`
  | `${typeof OUTPUT_TOTAL_PRICE}${OutputSeparator}${Space}${string}`
let outputDisplay: OutputDisplayText[] = []

type Props = PropsWithChildren<{ comboBoxData: EntriesProps }>
export const Playground = ({ comboBoxData }: Props) => {
  async function add(formData: FormData) {
    "use server"

    const formDataEntries = formData.entries()

    //   skip next js noise
    formDataEntries.next()

    const res: InputData = {
      label: "" as InputDisplayText,
      value: "",
    }

    for (let [key, value] of formDataEntries) {
      value = value.toString()
      let [v, label = ""] = value.split(VALUE_SEPARATOR)
      label = label.trim()

      switch (key as Keys[number]) {
        case "measurement_type":
          label += " of"
          if (!v) label = ""
          break

        case "tax_type":
          label = `${label.toLowerCase()}ed`
          if (!v) label = ""
          break

        case "product_type":
          label = INPUT_SEPARATOR
          break

        default:
          label = label || v
          break
      }
      res.value += `${v}${POST_SEPARATOR}`
      res.label += `${label}${SPACE}`
    }

    res.value = res.value.slice(0, -1)
    inputDisplay.push(res)
    revalidatePath("/")
  }

  async function submit(formData: FormData) {
    "use server"

    const formValues = formData.values()
    // skip noise
    formValues.next()

    type Payload = Record<`${Keys[number]}s`, (string | number)[]>
    let payload: Payload = entriesOutputKeys.reduce((a, v) => {
      a[`${v}s`] = []

      return a
    }, {} as Payload)

    for (let value of formValues) {
      value = value as string
      const inputs = value.split(POST_SEPARATOR)
      let i = 0

      for (const key of entriesOutputKeys) {
        const data = inputs[i]
        payload[`${key}s`].push(Number(data) || data)

        i = i + 1
      }
    }

    let response = await postJSON("http://127.0.0.1:3000/api/entries", payload)

    let data = await response.json()
    outputDisplay = displayOutput(
      inputDisplay.map((v) => v.label),
      data,
    ) as OutputDisplayText[]

    revalidatePath("/")
  }

  return (
    <>
      <form className="flex gap-2" action={add}>
        <Input
          type="number"
          min={0}
          id={entriesOutputKeys[0]}
          placeholder="Insert amount..."
          name={entriesOutputKeys[0]}
          required
        />
        <Combobox
          key={entriesOutputKeys[1]}
          name={entriesOutputKeys[1]}
          data={comboBoxData["measurements"]}
        />
        <Combobox
          key={entriesOutputKeys[2]}
          name={entriesOutputKeys[2]}
          data={comboBoxData["taxes"]}
        />
        <Input
          type="text"
          id={entriesOutputKeys[3]}
          placeholder="Insert product name..."
          name={entriesOutputKeys[3]}
          required
        />
        <Combobox
          key={entriesOutputKeys[4]}
          name={entriesOutputKeys[4]}
          data={comboBoxData["kinds"]}
          required
        />
        <Input
          type="number"
          min={0.0}
          step="0.01"
          id={entriesOutputKeys[5]}
          placeholder="Insert price..."
          name={entriesOutputKeys[5]}
          required
        />
        <Button>Add</Button>
      </form>
      <form className="w-full" action={submit}>
        <Button type="submit">
          <SendHorizonal />
        </Button>
        {Boolean(inputDisplay.length) && (
          <>
            <h2>{INPUT_TITLE}</h2>
            {inputDisplay.map((v, i) => (
              <>
                <input
                  type="hidden"
                  name={`data${i}`}
                  value={v.value}
                  required
                />
                <Input value={v.label} key={i} disabled />
              </>
            ))}
          </>
        )}
        {Boolean(outputDisplay.length) && (
          <>
            <br />
            <br />
            <Separator />
            <br />
            <h2>{OUTPUT_TITLE}</h2>
            {outputDisplay?.map((text, i) => (
              <Input value={text} key={i} disabled />
            ))}
          </>
        )}
      </form>
    </>
  )
}

function displayOutput(listOfString: InputDisplayText[], data: EntriesOutput) {
  const result = listOfString.map((text, i) => {
    let result = text.split(INPUT_SEPARATOR)[0].trimEnd()

    return `${result}${OUTPUT_SEPARATOR}${SPACE}${data.prices[i]}`
  })

  result.push(
    `${OUTPUT_TOTAL_TAX}${OUTPUT_SEPARATOR}${SPACE}${data.total_tax}`,
    `${OUTPUT_TOTAL_PRICE}${OUTPUT_SEPARATOR}${SPACE}${data.total_price}`,
  )

  return result
}
