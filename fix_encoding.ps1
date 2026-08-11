 = Get-ChildItem -Filter *.html
 = [System.Text.Encoding]::UTF8.GetString([byte[]](0xC3, 0xA2, 0xE2, 0x82, 0xAC, 0xC2, 0x9D))

foreach ($file in $files) {
    $text = [System.IO.File]::ReadAllText($file.FullName)
    
    $updated = $text.Replace('â†’', '→')
    $updated = $updated.Replace('â”¬âŒ ', '©')
    $updated = $updated.Replace('â€”', '—')
    $updated = $updated.Replace('â€¢', '•')
    $updated = $updated.Replace('â€œ', '“')
    $updated = $updated.Replace($mangledRightQuote, '”')

    if ($text -ne $updated) {
        Write-Host "Fixed $($file.Name)"
        [System.IO.File]::WriteAllText($file.FullName, $updated)
    }
}
