---
type: architecture
status: status/active
source: recovered-from-session
tags: [type/architecture, type/pattern, discipline/code]
publish: true
---

# World Streaming — Box Zones

How chunks load and unload in an open world with tall levels.

## The bug

`SceneRegion` originally measured the distance from the player to a single point, the chunk's centre, and toggled the chunk using an enter and exit radius.

A sphere around a point works for a flat, roughly square area. It does not work for a tall, thin level.

If the chunk centre is at mid-height and the player climbs to the top, they move away from that centre. Once they pass `ExitRadius`, the chunk they are standing in switches off and the world disappears under them.

In a game built on vertical traversal, this is not an edge case.

![[diagram-box-vs-sphere-streaming.svg]]

## The fix

Measure the distance to a box that wraps the whole chunk, including its full height.

When the player is inside the box, the distance is zero. So it does not matter how high they climb — they are still at the chunk and it stays active. The chunk only fades to preview once they leave the box and move away from it.

```csharp
private float DistanceToZone(Vector3 point)
{
    if (_zone != null) return Mathf.Sqrt(_zone.bounds.SqrDistance(point));
    return Vector3.Distance(point, transform.position);   // fallback
}
```

## Setup

1. On each chunk root, add a `BoxCollider` and tick **Is Trigger**.
2. Scale it to enclose the entire chunk. Tall and thin for a vertical level.
3. Drag it into the `_zone` slot.
4. `EnterRadius` and `ExitRadius` are now margins around the box, not chunk size. Try 5 and 15.

## Two things this gives for free

The chunk the player is inside never deactivates, because the distance is always zero. In The Big Catch this required a separate safety volume system.

Stacked chunks hand off cleanly. Split a tall tower into several chunks, give each a box covering its height band, and overlap them slightly. Climbing from one box into the next is seamless.

## The general point

Match the shape of the trigger volume to the shape of the level. A radius assumes the space is roughly spherical, and that assumption stays invisible until a player climbs something.

## Open questions

## Answered

*Questions that got settled. Keep the answer, not just the tick.*

## Related

[[World Model - Islands & Landmarks]] · [[Landmark-Driven Open World]] · [[The Big Catch - Tacklebox]]
