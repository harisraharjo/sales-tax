"use client"

import * as React from "react"
import { Check, ChevronsUpDown } from "lucide-react"

import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"
import {
  Command,
  CommandEmpty,
  CommandGroup,
  CommandInput,
  CommandItem,
} from "@/components/ui/command"
import {
  Popover,
  PopoverContent,
  PopoverTrigger,
} from "@/components/ui/popover"
import type { RawData, RawIdx } from "../../app/Playground"
import { VALUE_SEPARATOR } from "@/app/constants"

// const data = [
//   {
//     id: 1,
//     name: "Next.js",
//   },
//   {
//     id: 2,
//     name: "Svelte Kit",
//   },
//   {
//     id: 3,
//     name: "Nuxt.js",
//   },
//   {
//     id: 4,
//     name: "Remix",
//   },
//   {
//     id: 5,
//     name: "Astro",
//   },
// ]

export type InputValue = `${string}${typeof VALUE_SEPARATOR}${string}`

type Props = {
  name: string
  placeholder?: string
  data: { id: number; name: string }[]
  onSelect?: <T extends RawIdx>(i: T, v: RawData[T]) => any
  required?: true
}
export function Combobox({
  name,
  placeholder,
  onSelect,
  data,
  required,
}: Props) {
  const [open, setOpen] = React.useState(false)
  const [value, setValue] = React.useState("")
  const [label, setLabel] = React.useState("")

  return (
    <Popover open={open} onOpenChange={setOpen}>
      <PopoverTrigger asChild>
        <Button
          variant="outline"
          role="combobox"
          aria-expanded={open}
          className="w-[200px] justify-between"
        >
          <input type="hidden" name={name} value={value} required={required} />
          {label || "Select item..."}
          <ChevronsUpDown className="ml-2 h-4 w-4 shrink-0 opacity-50" />
        </Button>
      </PopoverTrigger>
      <PopoverContent className="w-[200px] p-0">
        <Command>
          <CommandInput placeholder="Search item..." />
          <CommandEmpty>No item found.</CommandEmpty>
          <CommandGroup>
            {data.map((item) => (
              <CommandItem
                key={item.id}
                onSelect={(currentValue) => {
                  const _label = data.find(
                    (v) => v.id === Number(currentValue),
                  )!.name

                  const labelResult = _label === label ? "" : _label
                  setLabel(labelResult)
                  setValue(
                    !labelResult
                      ? labelResult
                      : `${currentValue}${VALUE_SEPARATOR}${labelResult}`,
                  )
                  onSelect?.(item.id as RawIdx, item.name)
                  setOpen(false)
                }}
                value={String(item.id)}
              >
                <Check
                  className={cn(
                    "mr-2 h-4 w-4",
                    value === item.name ? "opacity-100" : "opacity-0",
                  )}
                />
                {item.name}
              </CommandItem>
            ))}
          </CommandGroup>
        </Command>
      </PopoverContent>
    </Popover>
  )
}
