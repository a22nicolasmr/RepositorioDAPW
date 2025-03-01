<?php

declare(strict_types=1);

namespace Drupal\entity_test\Plugin\Field\FieldWidget;

use Drupal\Core\Field\Attribute\FieldWidget;
use Drupal\Core\Field\FieldItemListInterface;
use Drupal\Core\Field\WidgetBase;
use Drupal\Core\Form\FormStateInterface;
use Drupal\Core\StringTranslation\TranslatableMarkup;

/**
 * Plugin implementation of the 'shape_only_color_editable_widget' widget.
 */
#[FieldWidget(
  id: 'shape_only_color_editable_widget',
  label: new TranslatableMarkup('Shape widget with only color editable property'),
  field_types: ['shape'],
)]
class ShapeOnlyColorEditableWidget extends WidgetBase {

  /**
   * {@inheritdoc}
   */
  public function formElement(FieldItemListInterface $items, $delta, array $element, array &$form, FormStateInterface $form_state) {
    $element['shape'] = [
      '#type' => 'hidden',
      '#value' => $items[$delta]->shape,
    ];

    $element['color'] = [
      '#type' => 'textfield',
      '#default_value' => $items[$delta]->color ?? NULL,
      '#size' => 255,
    ];

    return $element;
  }

}
