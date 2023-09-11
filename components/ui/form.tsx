import * as React from "react"

import { cn } from "@/lib/utils"

const FormItem = ({ children }: React.PropsWithChildren) => {
  return <div className={cn("space-y-2")}>{children}</div>
}

// const FormDescription = () => {
//   return (
//     <p
//       ref={ref}
//       id={formDescriptionId}
//       className={cn("text-sm text-muted-foreground", className)}
//       {...props}
//     />
//   )
// }

// const FormMessage = React.forwardRef<
//   HTMLParagraphElement,
//   React.HTMLAttributes<HTMLParagraphElement>
// >(({ className, children, ...props }, ref) => {
//   const { error, formMessageId } = useFormField()
//   const body = error ? String(error?.message) : children

//   if (!body) {
//     return null
//   }

//   return (
//     <p
//       ref={ref}
//       id={formMessageId}
//       className={cn("text-sm font-medium text-destructive", className)}
//       {...props}
//     >
//       {body}
//     </p>
//   )
// })
// FormMessage.displayName = "FormMessage"

export { FormItem }
