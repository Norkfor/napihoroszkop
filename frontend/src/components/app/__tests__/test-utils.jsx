import React from 'react'
import { render } from '@testing-library/react'

export function renderWithProps(ui, props = {}, options = {}) {
  const utils = render(React.cloneElement(ui, props), options)
  return { ...utils }
}
