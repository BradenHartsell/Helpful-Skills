# Theming and design system

## Contents

- Extend the existing owner
- Token architecture
- Color roles and contrast
- Typography
- Shape
- Elevation
- Dynamic and brand color
- Theme implementation pattern
- Theme validation

## Extend the existing owner

Find the repository's canonical theme before adding any value. Inspect:

- `MaterialTheme` setup and custom composition locals;
- light, dark, and high-contrast palettes;
- typography and bundled fonts;
- shape scale;
- spacing, size, motion, and elevation tokens;
- canonical buttons, fields, cards, navigation, and feedback components;
- screenshot, preview, or theme tests.

Extend this owner directly. A feature-level nested theme is appropriate only when the product intentionally creates a contained visual context and the ownership is explicit.

## Token architecture

Keep raw values below semantic roles:

```text
raw palette, font, dimension, motion values
  -> semantic product roles
  -> component configuration
  -> screen composition
```

Example semantic categories:

| Category | Example roles |
|---|---|
| Color | `contentPrimary`, `contentMuted`, `surfaceBase`, `surfaceRaised`, `actionPrimary`, `actionDestructive`, `focusRing` |
| Type | `screenTitle`, `sectionTitle`, `bodyPrimary`, `bodySupporting`, `controlLabel`, `numericStatus` |
| Space | `screenInset`, `sectionGap`, `contentGap`, `controlGap`, `paneGap` |
| Shape | `containerPrimary`, `containerSupporting`, `controlPrimary`, `selectionIndicator` |
| Motion | `feedbackFast`, `layoutDefault`, `revealSlow`, `reducedMotionFade` |
| Size | `interactiveMinimum`, `contentReadableMax`, `navigationWidth`, `paneMinimum` |

Do not expose arbitrary raw values as the main screen API. Do not turn every number into a global token. A token earns global ownership when its purpose is shared and call sites should change together.

## Color roles and contrast

Use semantic pairs. An `on` role belongs on its matching parent or container role.

| Role family | Typical purpose |
|---|---|
| Primary | highest-emphasis actions and key selected states |
| Secondary | less prominent actions and supporting emphasis |
| Tertiary | smaller special accents, contrast, or expressive moments |
| Error | destructive, invalid, or critical error states |
| Surface | app background and content hierarchy |
| Surface containers | nested or elevated content regions |
| Inverse | transient content that must contrast with the surrounding surface, such as a snackbar |
| Outline | important boundaries and control outlines |
| Outline variant | quiet dividers and decorative boundaries |

Rules:

- Preserve paired foreground and background roles.
- Avoid using primary color on every interactive item.
- Use surface tone to establish hierarchy before introducing more accent colors.
- Preserve semantic brand colors when dynamic color would alter their meaning.
- Communicate selection, validation, and severity with text, iconography, shape, or structure in addition to color.
- Verify rendered contrast, including disabled and high-contrast variants.

Material guidance uses at least 4.5:1 for small body text, 3:1 for large text, and commonly 3:1 for meaningful non-text controls or boundaries. Treat these as minimum checks, not a complete accessibility verdict.

## Typography

Material 3's baseline roles are organized into display, headline, title, body, and label families, each with large, medium, and small variants. Current expressive guidance also offers emphasized counterparts.

Choose roles by function:

- display and large headline for rare hero or editorial moments;
- headline and title for hierarchy and navigation context;
- body for sustained reading and explanation;
- label for controls, metadata, and compact status.

Use emphasized type selectively for a selected item, unread state, key action, or important headline. Do not use it for every label.

Typography quality rules:

- use a distinctive brand face primarily for larger roles;
- use a highly readable face for body and controls;
- provide font fallbacks and verify every target;
- avoid decorative type for forms and dense operational content;
- preserve text scaling and avoid fixed-height containers around text;
- keep large text near a 1.2 line-height ratio and body copy near 1.5 as a starting point, then validate the actual font;
- use tabular figures for changing numeric values when the font supports them;
- style links with an underline plus semantic link color;
- keep editorial treatments out of component labels.

## Shape

Use shape to reinforce hierarchy and product character.

- Give repeated components consistent shape roles.
- Let a primary or celebratory surface carry the strongest shape expression.
- Use asymmetry or unusual geometry only when content remains legible and the interaction remains obvious.
- Do not use shape as the sole signal for state or meaning.
- Reserve abstract shapes mostly for imagery and decoration.
- Use shape morphing only when it explains state, progress, or a spatial relationship.

Material 3 Expressive expands the available shape vocabulary, but a design can use that vocabulary through stable primitives without requiring a named expressive component API.

## Elevation

Use elevation to explain layering:

- tonal surface differences for persistent hierarchy;
- shadow for floating, overlapping, or transient content;
- scrims for modal focus;
- a minimal number of levels per screen.

Avoid stacking multiple elevated containers with no spatial reason. A border, tonal surface, spacing, or heading may group content more clearly.

## Dynamic and brand color

Dynamic color can derive from wallpaper, content, or a user-selected source. It is not automatically appropriate for every product or target.

- Keep dynamic color behind the canonical theme owner.
- Preserve fixed semantic colors for brand identity, error meaning, financial direction, or other product-specific semantics.
- If deriving color from content, keep the relationship spatially clear.
- Validate light, dark, and contrast behavior after derivation.
- Provide a stable fallback when the platform cannot supply dynamic color.

## Theme implementation pattern

Prefer one app theme that configures Material roles and exposes only truly product-specific tokens:

```kotlin
@Immutable
data class ProductSpacing(
    val screenInset: Dp,
    val sectionGap: Dp,
    val contentGap: Dp,
)

private val LocalProductSpacing = staticCompositionLocalOf<ProductSpacing> {
    error("ProductSpacing is not provided")
}

val MaterialTheme.productSpacing: ProductSpacing
    @Composable get() = LocalProductSpacing.current
```

This is a structural example, not an instruction to add a new spacing system when one already exists.

Keep theme selection above screen composition:

```kotlin
@Composable
fun ProductTheme(
    darkTheme: Boolean,
    content: @Composable () -> Unit,
) {
    CompositionLocalProvider(
        LocalProductSpacing provides productSpacing,
    ) {
        MaterialTheme(
            colorScheme = if (darkTheme) darkScheme else lightScheme,
            typography = productTypography,
            shapes = productShapes,
            content = content,
        )
    }
}
```

Verify the exact imports and API signatures against the installed Compose version.

## Theme validation

Review representative screens in:

- light and dark themes;
- the platform's contrast preference when supported;
- compact and wide windows;
- normal and increased text size;
- normal, focused, hovered, pressed, selected, disabled, error, and loading states;
- at least one dense surface and one empty or low-content surface;
- every bundled font target.

Inspect whether:

- foreground and container roles remain paired;
- focus remains visible on every surface;
- typography establishes a clear first read;
- long text wraps without clipping;
- surfaces form a coherent hierarchy;
- custom colors and shapes have semantic owners;
- target rendering differences change line breaks, control size, or rhythm.
