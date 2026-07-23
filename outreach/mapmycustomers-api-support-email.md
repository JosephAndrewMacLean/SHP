# Email — MapMyCustomers API & Support

**To:** support@mapmycustomers.com; api@mapmycustomers.com _(confirm correct addresses — see note below)_
**From:** jmaclean@synergyhealth.org
**Subject:** API access, documentation, and a data-integration request — Synergy Health Partners

---

Hello MapMyCustomers Team,

My name is Joe MacLean, and I manage [marketing / digital operations] at **Synergy
Health Partners**, a healthcare organization currently using MapMyCustomers to support
our field-based physician-liaison (PL) and referral-development work.

Our account is registered under **[ACCOUNT / ORGANIZATION NAME]** ([primary account
email on file]). We're working to streamline two things for our liaison team: **(a) how
quickly they can import and update account data**, and **(b) how they flag whether an
account is a good fit for our spine service line** so we can prioritize and report on it.
We'd appreciate your team's help with the four items below, which support those goals.
I've separated them so the right people can pick up each one — happy to open individual
tickets if that's easier on your end.

## 1. API access & credentials

We'd like to enable programmatic access to our account so we can integrate MapMyCustomers
data with our internal reporting and analytics stack. Could you let us know:

- Whether API access is included on our current plan, or requires an upgrade / add-on.
- The steps to provision an **API key / access token** for our account.
- Who on our side needs to authorize the request (admin/owner), and any security or
  agreement steps (e.g., a data-processing or BAA-style agreement) we should complete
  first. As a healthcare organization, data handling and access controls matter to us,
  so we'd want to get that right up front.

## 2. API documentation & capabilities

Before we build anything, we'd like to understand what the API supports. Could you share
or point us to:

- **Full API documentation** (endpoints, authentication method, request/response formats).
- Which objects and fields are exposed — e.g., accounts/companies, contacts, activities,
  territories, routes, check-ins, and **custom fields**.
- **Custom fields specifically:** can we create and read/write our own fields (e.g., a
  "Spine fit" status or a "not a fit for spine" flag) via the API and via bulk import,
  and can we filter/segment/report on those fields?
- **Bulk import:** the supported ways to import and *update* records in volume —
  spreadsheet/CSV upload, the API, or both — including how records are matched on import
  to avoid creating duplicates.
- **Rate limits**, pagination, and whether the API supports both **read and write**
  (pull *and* push) operations.
- Any **webhooks or bulk/export endpoints** for keeping an external system in sync.

## 3. Import workflow & spine-fit flagging (our main goal)

The outcome we're after is a faster, cleaner workflow for our physician liaisons. Two
specific use cases:

- **Faster data import for PLs.** Today, getting account and contact data into the
  platform is [manual / slow — describe current process]. We'd like the most efficient
  supported way for liaisons to **import and update accounts in bulk** — via
  spreadsheet/CSV, the API, or an integration — with **duplicate matching** so we're
  updating existing records rather than creating new ones.
- **Flagging accounts by spine fit.** We want liaisons to be able to mark whether an
  account is a **good fit (or not) for our spine service line** — e.g., a dedicated
  custom field or tag — and then **filter, route, and report** on that flag. Ideally a
  PL can set this in the field (mobile app) and we can also **set it in bulk on import**
  for accounts we've already assessed.

Could you advise on the best supported path for each — native fields/tags, bulk import,
the API, or a partner connector — and whether any of it depends on our current plan? If
you offer a one-time **full data export** of our account (so we can reconcile and re-import
cleanly), we'd like to request that as well.

## 4. Technical issue

We're also running into a problem we'd like your support team to look into:

- **Issue:** [Describe what's happening — the specific feature/screen, what you expected,
  and what actually occurs.]
- **When it started / how often:** [Date first noticed; every time vs. intermittent.]
- **Users / accounts affected:** [Names or count of affected users.]
- **Steps to reproduce:** [1) … 2) … 3) …]
- **Environment:** [Web browser + version, and/or iOS/Android app version.]

I'm glad to send screenshots, a screen recording, or example record IDs — just let me know
what's most useful for diagnosis.

---

If it's easier to cover the API and integration questions on a short call, I'm happy to
set one up. Otherwise, written pointers to the right documentation and next steps would be
much appreciated.

Thank you for your help — I look forward to hearing from you.

Best regards,

Joe MacLean
[Title]
Synergy Health Partners
jmaclean@synergyhealth.org
[Phone]

---

### Notes before sending (delete this section)

- **Confirm the recipient addresses.** MapMyCustomers' general support is typically
  reached at `support@mapmycustomers.com` or via in-app chat / their help center; there
  may not be a public `api@` inbox. Verify the correct API/developer contact — the in-app
  support chat is often the fastest route, and they can direct the API request internally.
- **Fill every `[BRACKETED]` placeholder** — especially account name, the description of
  your PLs' current import process (Section 3), and the bug details (Section 4). Delete
  Section 4 entirely if you don't currently have a technical issue to report.
- **Consider splitting** the technical issue (Section 4) into its own ticket if you want
  it triaged quickly — access/API/integration questions often route to a different team
  than break/fix support, so a combined email can slow the bug down.
