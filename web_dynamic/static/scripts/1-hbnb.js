$(document).ready(function() {
    $('input[type="checkbox"]').change(function() {
        var selectedAmenities = [];
        $('input[type="checkbox"]:checked').each(function() {
            var amenityId = $(this).data('id');
            var amenityName = $(this).data('name');
            selectedAmenities.push(amenityName);
        });
        $('#selected-amenities-list').text(selectedAmenities.join(', '));
    });
});
