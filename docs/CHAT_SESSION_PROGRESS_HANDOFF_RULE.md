# Chat Session Progress + Automatic Handoff Protocol

Status: PROJECT-WIDE OPERATING RULE

This rule exists to prevent active localization/QC work from being lost when a long ChatGPT conversation approaches its usable context/session limit.

## 1. Progress indicator on every assistant reply

For every reply during this project, append a compact approximate session-capacity indicator, for example:

`会话容量（估算）：███░░░░░░░ 约30%`

Important: ChatGPT does not expose a reliable exact user-visible hard-limit counter to the assistant. The indicator is therefore a conservative estimate of conversation/context pressure, not a guaranteed exact token percentage.

## 2. Automatic handoff before the danger zone

Do not wait for the user to request a handoff once the conversation is clearly approaching the danger zone. Proactively prepare a complete handoff before continuity becomes unreliable.

The handoff must preserve:

- current task / component and exact status;
- approved / rejected revisions and why;
- exact Mother/output hashes and PathIDs when relevant;
- current translations and locked wording;
- typography/layout/QC rules currently in force;
- unresolved problems and exact next action;
- all relevant GitHub state/commits created during the session.

## 3. Active visual/material work must be bundled

If the session is currently editing a baked UI texture, atlas, image asset, or similar visual material, the handoff must NOT contain text only.

Create one handoff bundle containing, where applicable:

- current canonical original/source raster;
- approved clean plate / clean slate;
- latest accepted candidate and latest rejected candidate when diagnostically useful;
- exact recovered source layers (for example canonical Normal/Selected text rasters);
- white-background QC;
- black-background QC;
- mandatory overlay comparison;
- mandatory top/bottom outer-envelope line-spacing comparison;
- measurement JSON/CSV;
- deterministic generation/rebuild script or recipe sufficient to continue the work;
- hashes for the included files;
- a human-readable handoff prompt/document explaining which files are canonical.

Do not package proprietary complete game assets into the public GitHub repository. A private conversation handoff bundle may contain user-supplied/current-working extracted visual files required for continuity, but public repository rules remain unchanged.

## 4. Fail closed

If a canonical working file cannot be recovered or included, state exactly what is missing. Do not claim a handoff is complete while silently substituting an approximation.

## 5. Handoff interaction rule

When the danger zone is reached during an active task:

1. finish the smallest safe atomic QC step if possible;
2. generate the handoff prompt/document;
3. generate the active-work bundle;
4. provide both to the user and explicitly recommend opening a new conversation with them;
5. do not begin a large new subtask in the old conversation after the handoff is prepared.
