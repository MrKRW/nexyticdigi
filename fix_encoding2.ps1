$files = Get-ChildItem -Filter *.html
$mangledRightQuote = [System.Text.Encoding]::UTF8.GetString([byte[]](0xC3, 0xA2, 0xE2, 0x82, 0xAC, 0xC2, 0x9D))

foreach ($file in $files) {
    $text = [System.IO.File]::ReadAllText($file.FullName)
    
    $updated = $text.Replace('→', [char]0x2192)
    $updated = $updated.Replace('┬� ', [char]0x00A9)
    $updated = $updated.Replace('—', [char]0x2014)
    $updated = $updated.Replace('•', [char]0x2022)
    $updated = $updated.Replace('“', [char]0x201C)
    $updated = $updated.Replace($mangledRightQuote, [char]0x201D)

    if ($text -ne $updated) {
        Write-Host "Fixed $($file.Name)"
        [System.IO.File]::WriteAllText($file.FullName, $updated)
    }
}
