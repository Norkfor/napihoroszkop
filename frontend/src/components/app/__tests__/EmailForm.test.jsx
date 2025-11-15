import React from 'react'
import { describe, it, expect, vi, beforeEach, afterEach } from 'vitest'
import { render, screen, fireEvent, waitFor } from '@testing-library/react'
import EmailForm from '../EmailForm'

describe('EmailForm', () => {
  beforeEach(() => {
    globalThis.fetch = vi.fn()
  })

  afterEach(() => {
    vi.restoreAllMocks()
  })

  it('renders email input and button', () => {
    render(<EmailForm name="Teszt" month={1} day={1} />)
    expect(screen.getByPlaceholderText('Email')).toBeTruthy()
    expect(screen.getByRole('button', { name: /Feliratkozom/i })).toBeTruthy()
  })

  it('validates email and shows error', async () => {
    render(<EmailForm name="Teszt" month={1} day={1} />)
    fireEvent.click(screen.getByRole('button', { name: /Feliratkozom/i }))
    expect(await screen.findByText(/Adj meg egy e-mail címet!/i)).toBeTruthy()
  })

  it('posts to backend when valid', async () => {
    const fakeRes = { message: 'Siker' }
    globalThis.fetch.mockResolvedValueOnce({ ok: true, json: async () => fakeRes })

    render(<EmailForm name="Teszt" month={1} day={1} />)
    fireEvent.change(screen.getByPlaceholderText('Email'), { target: { value: 'a@b.com' } })
    fireEvent.click(screen.getByRole('button', { name: /Feliratkozom/i }))

    await waitFor(() => expect(globalThis.fetch).toHaveBeenCalled())
    expect(await screen.findByText(/Siker/i)).toBeTruthy()
  })
})
